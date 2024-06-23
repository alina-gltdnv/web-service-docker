FROM python:3

#WORKDIR /usr/src/app

RUN git clone https://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@github.com/alina-gltdnv/web-service-docker.git

RUN pip install -r ./web-service-docker/requirements.txt

CMD [ "python3", "./web-service-docker/target_heart_rate.py" ]