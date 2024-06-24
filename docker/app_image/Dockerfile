FROM python:3

#WORKDIR /usr/src/app

COPY target_heart_rate.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python3", "./target_heart_rate.py" ]