import requests
import time
import random


def target_heart_rate():
    age = random.randint(a=1, b=100)
    url = "0.0.0.0:5000/calculations/target-heart-rate"
    header = {"Content-Type": "application/json"}
    data = {"age": age }
    resp = requests.post(url=url, headers=header, data=data)


if __name__ == '__main__':
    try:
        while True:
            target_heart_rate()
            time.sleep(1)
    except Exception as e:
        print(e)
