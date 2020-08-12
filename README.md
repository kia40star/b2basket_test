# b2basket_test
Django-celery-docker

# Порядок запуска:

- docker-compose up -d --build db
- docker-compose up -d --build redis
- docker-compose up -d --build web
- docker-compose up -d --build celery

# Тестирование:
- ./test.sh

# Описание API:
- BASE_URL = 127.0.0.1:8000
- GET BASE_URL/urls/
- GET BASE_URL/urls/id/
- POST BASE_URL/urls/ {"url": string}
- GET BASE_URL/keys/
- GET BASE_URL/keys/id/