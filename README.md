# Intelligence Manufacturing System

# How to run project

## Fill .env file using .env.example

## Activate virtual environment and Install all dependencies

```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## 1. Project database is working in docker, firstly run the docker

```shell
$ docker-compose -f db-compose.yml up --build
```

## 2. Migrate all migrations

```shell
$ python manage.py migrate
```

## Run project

```shell
$ python manage.py runserver
```