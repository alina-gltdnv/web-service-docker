#!/bin/sh

echo "Checking docker installation"
if command -v docker &> /dev/null; then
    echo "Docker installation found"
else
    echo "Docker installation not found. Installing..."
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
fi

echo "Cloning Signoz"
git clone -b main https://github.com/SigNoz/signoz.git

echo "Replacing docker-compose.yaml for Signoz"
cp -fr ./web-service-docker/docker/signoz_compose/docker-compose.yaml ./signoz/deploy/docker/clickhouse-setup

echo "Replacing otel-collector-config.yaml for Signoz"
cp -fr ./web-service-docker/docker/signoz_compose/otel-collector-config.yaml ./signoz/deploy/docker/clickhouse-setup

echo "Creating dir for Prometheus logs"
sudo mkdir prometheus_data

echo "Building docker image for App"
sudo docker build --no-cache -t app ./web-service-docker/docker/app_image/

echo "Starting Signoz"
sudo docker compose -f ./signoz/deploy/docker/clickhouse-setup/docker-compose.yaml up -d

echo "Starting App + Prometheus"
sudo docker compose -f ./web-service-docker/docker/app_prometheus_compose/docker-compose.yml up -d