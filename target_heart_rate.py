from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Summary, Counter
import time

app = Flask(__name__)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


@app.route('/calculations/target-heart-rate', methods=['POST'])
@REQUEST_TIME.time()
def thr_service():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    age = data.get('age')
    if not isinstance(age, int):
        try:
            age = int(age)
        except (ValueError, TypeError):
            return jsonify({"error": "Age must be an integer"}), 400

    if age < 18 or age > 99:
        return jsonify({"error": "Enter an age greater than 17 and less than 100"}), 400

    lower, upper = thr_counter(age)
    response = {
        "targetHeartRate": {
            "lowerBound": lower,
            "upperBound": upper
        }
    }
    return jsonify(response), 200


def thr_counter(age):
    max_hr = 220 - age
    lower_bound = 0.5 * max_hr
    upper_bound = 0.85 * max_hr
    return lower_bound, upper_bound


if __name__ == '__main__':
    start_http_server(8333)
    app.run(debug=False, host='0.0.0.0', port=5000)
