#!/usr/bin/env bash

docker-compose pull
docker-compose -f docker-compose.yml -f production.yml up -d
