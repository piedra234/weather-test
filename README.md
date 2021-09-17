## Weather_test for Globant 
==========================
This is a repository containing test for globant application

## Deployment
If you want to deploy service this is the flow you want to follow:


1. First create an environment file .env containing following information
```bash
## Postgres 
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

## Django
DEBUG=True
SECRET_KEY=django-key
APICACHE_SECONDS=300
SCHEDULER_AUTOSTART=False
```

2. Configure Postgres. Create an db instance with command 
```bash
$ docker-compose -f docker-init.yml up --build
```


3. Initialize the containers with docker compose
```bash
$ docker-compose -f docker-compose.yml up --build
```

4. Configure Django. Open another terminal in same path and execute migrations and createsuperuser
`$ docker ps` -> to get <NAME> of container
```bash
$ docker exec -it <NAME> python manage.py makemigrations
$ docker exec -it <NAME> python manage.py migrate
$ docker exec -it <NAME> python manage.py createsuperuser
```

5. Stop containers in the fisrt terminal

6. Modify .env and set `SCHEDULER_AUTOSTART=True` to start scheduler

7. Initialize the containers with docker compose to load changes
```bash
$ docker-compose -f docker-compose.yml up
```

8. Run testCase on second terminal (Optional) 
```bash
$ docker exec -it <NAME> python manage.py test
```

## Developments

### db: PostgreSQL 13.4
### web: Python 3.9.7 / Django version 3.2.7
- `framework: Django REST` https://www.django-rest-framework.org/
- `logging: Django Request Logging` https://pypi.org/project/django-request-logging/
- `jobs: Django APScheduler` https://pypi.org/project/django-apscheduler/0.6.0/

## URL
- GET `/weather?city=$City&country=$Country`

- PUT `/scheduler/weather` {“city”: $City, “country”: $Country}, content_type='application/json'