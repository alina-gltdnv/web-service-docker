FROM python:3

#WORKDIR /usr/src/app

COPY web-service-docker/target_heart_rate.py .
COPY web-service-docker/requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python3", "./target_heart_rate.py" ]