#!/bin/bash
# Run Django with Gunicorn for production
source venv/bin/activate
python manage.py collectstatic --noinput
gunicorn crudapp.wsgi:application --bind 0.0.0.0:8000 --workers 4