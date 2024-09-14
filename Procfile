web: gunicorn todo_drf.wsgi --log-file - 

web: python manage.py migrate && gunicorn todo_drf.wsgi