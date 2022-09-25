#!/bin/bash


python3 manage.py migrate
python3 manage.py createcachetable
python3 manage.py collectstatic --noinput

if [ "$DEPLOY" = "TRUE" ]; then
    echo "------------------------------------------------------------------------------------"
    echo "RUNNING DEPLOY"
    echo "------------------------------------------------------------------------------------"
    gunicorn --workers 4 --threads 4 root.wsgi --bind [::]:8000 --log-level=debug \
     --access-logfile '-' --error-logfile '-' \
     --access-logformat "%(m)s: %(U)s - %(s)s"
else
    echo "------------------------------------------------------------------------------------"
    echo "RUNNING TEST"
    echo "------------------------------------------------------------------------------------"
    gunicorn --workers 2 --threads 2 root.wsgi --bind [::]:8000 --reload --log-level=debug \
     --access-logfile '-' --error-logfile '-' \
     --access-logformat "%(m)s: %(U)s - %(s)s"
fi