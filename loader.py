import requests
import time
import random
import json


def target_heart_rate():
    age = random.randint(a=1, b=100)
    url = "http://localhost:5000/calculations/target-heart-rate"
    header = {"Content-Type": "application/json"}
    data = {"age": age}
    resp = requests.post(url=url, headers=header, data=json.dumps(data))
    return data, resp.text, resp.elapsed.total_seconds()


if __name__ == '__main__':
    try:
        while True:
            req, resp, dur = target_heart_rate()
            print(f"req {req}, resp {resp}, dur {dur}")
            time.sleep(1)
    except Exception as e:
        print(e)
