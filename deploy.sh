#!/usr/bin/env bash

docker-compose pull
#docker-compose -f docker-compose.yml -f production.yml up -d

docker-compose -f docker-compose.yml -f production.yml config > full_production.yml
docker stack deploy --compose-file full_production.yml pythonathon
