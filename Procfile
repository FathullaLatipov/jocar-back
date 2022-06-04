release: python manage.py migrate

web: gunicorn jocar.wsgi --log-file -

worker: python manage.py rqworker default