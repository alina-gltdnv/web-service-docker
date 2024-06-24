# Web-service-docker

## Overview
This project contains a Python Flask web-service that uses the Prometheus-client for monitoring and visualization in Signoz.

## Installation
To get started with this project, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/alina-gltdnv/web-service-docker.git
```
2. Run [setup.sh](setup.sh) to set up the environment and build Docker containers:
```bash
sudo chmod +x ./web-service-docker/setup.sh
sudo ./web-service-docker/setup.sh
```

## Usage
After the containers are up and running, you can access the following services:

- Flask Web-Service: http://localhost:5000
- Prometheus: http://localhost:9090
- Signoz: http://localhost:3301

## Monitoring
The Flask web-service exposes metrics using Prometheus-client, which are collected and visualized in Signoz.

Use [metrics.json](signoz_dashboard/metrics.json) to import dashboard to your Signoz web interface.

## Test
Run [loader.py](loader.py) to send traffic to the service.
```bash
python3 ./web-service-docker/loader.py
```