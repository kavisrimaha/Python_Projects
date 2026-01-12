@echo off
REM Run Django with Gunicorn for production
call venv\Scripts\activate.bat
python manage.py collectstatic --noinput
gunicorn crudapp.wsgi:application --bind 0.0.0.0:8000 --workers 4