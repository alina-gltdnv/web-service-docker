from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Summary, Counter
import time

app = Flask(__name__)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


@app.route('/submit', methods=['POST'])
@REQUEST_TIME.time()
def submit():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    response = {
        "message": "Request received",
    }
    return jsonify(response), 200


if __name__ == '__main__':
    start_http_server(8000)
    app.run(debug=True, host='0.0.0.0', port=5000)

