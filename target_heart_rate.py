from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Histogram, Counter
import time

app = Flask(__name__)

REQUEST_TIME = Histogram('request_processing_seconds', 'Time spent processing request',
                         buckets=[0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.001, 0.002, 0.003, 0.004, 0.005, 0.01, 0.05,
                                  0.1, 0.5, 1, 2, 5, 10])
count_valid = Counter('requests_count_valid', 'The number of valid requests')
count_invalid = Counter('requests_count_invalid', 'The number of invalid requests')


@app.route('/calculations/target-heart-rate', methods=['POST'])
@REQUEST_TIME.time()
def thr_service():
    data = request.get_json()
    if not data:
        count_invalid.inc()
        return jsonify({"error": "No data provided"}), 400

    age = data.get('age')
    if not isinstance(age, int):
        try:
            age = int(age)
        except (ValueError, TypeError):
            count_invalid.inc()
            return jsonify({"error": "Age must be an integer"}), 400

    if age < 18 or age > 99:
        count_invalid.inc()
        return jsonify({"error": "Enter an age greater than 17 and less than 100"}), 400

    lower, upper = thr_counter(age)
    response = {
        "targetHeartRate": {
            "lowerBound": lower,
            "upperBound": upper
        }
    }
    count_valid.inc()
    return jsonify(response), 200


def thr_counter(age):
    max_hr = 220 - age
    lower_bound = 0.5 * max_hr
    upper_bound = 0.85 * max_hr
    return lower_bound, upper_bound


if __name__ == '__main__':
    start_http_server(8333)
    app.run(debug=False, host='0.0.0.0', port=5000)
