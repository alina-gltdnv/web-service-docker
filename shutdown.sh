#!/bin/sh

echo ":::::Stopping App + Prometheus:::::"
sudo docker compose -f ./web-service-docker/docker/app_prometheus_compose/docker-compose.yml down

echo ":::::Stopping Signoz:::::"
sudo docker compose -f ./signoz/deploy/docker/clickhouse-setup/docker-compose.yaml down