#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate
gunicorn manufacturing_system.wsgi:application --bind 0.0.0.0:8000

exec "$@"