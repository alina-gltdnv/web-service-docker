FROM python:3

#WORKDIR /usr/src/app

#RUN git clone https://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@github.com/alina-gltdnv/web-service-docker.git
COPY ./../../../target_heart_rate.py .

COPY ./../../../requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python3", "target_heart_rate.py" ]