#/bin/sh

docker-compose up --build -d
docker exec -it knewin_test_python_1 sh -c 'scrapy crawl -a teams_list=/app/list inter'
