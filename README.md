# Web-service-docker

Little docker project

## Run commands


```bash
# build docker image with flask app
sudo docker build --no-cache -t app /home/user/docker/image_test1/

# docker compose up - app with prometheus
sudo docker compose -f /home/user/docker/compose/docker-compose.yml up -d

# docker compose up - signoz
sudo docker compose -f /home/user/docker/signoz/deploy/docker/clickhouse-setup/docker-compose.yaml up -d
```
