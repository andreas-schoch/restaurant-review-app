#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
/opt/conda/envs/app/bin/gunicorn --bind 0.0.0.0:8000 project.wsgi