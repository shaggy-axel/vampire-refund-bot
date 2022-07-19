# RefBank Buyer Bot
## Stack
Python, Aiogram, Django,
Docker, PostgreSQL
## Setup
```bash
cat env_sample > .env
# change values in .env

docker-compose build
docker-compose up -d
docker-compose exec web sh -c "venv/bin/python src/manage.py migrate"
```

## Database migrations
```bash
# to make new migration files
docker-compose exec web sh -c "venv/bin/python src/manage.py makemigrations"
# run migrations
docker-compose exec web sh -c "venv/bin/python src/manage.py migrate"
```
