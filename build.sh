docker-compose build $@ &&
docker-compose push &&
docker-compose up -d &&
docker stats
