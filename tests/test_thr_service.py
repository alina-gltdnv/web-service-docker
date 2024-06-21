import pytest
import requests
import random

url = 'http://localhost:5000/calculations/target-heart-rate'


@pytest.mark.parametrize("age", [random.randint(1, 100) for _ in range(10)])
def test_thr_service(age):
    data = {'age': age}
    response = requests.post(url, json=data)

    assert response.status_code == 200
    json_response = response.json()
    assert 'targetHeartRate' in json_response
    assert 'lowerBound' in json_response['targetHeartRate']
    assert 'upperBound' in json_response['targetHeartRate']
    assert isinstance(json_response['targetHeartRate']['lowerBound'], float)
    assert isinstance(json_response['targetHeartRate']['upperBound'], float)