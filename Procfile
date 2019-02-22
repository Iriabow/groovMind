% prepara el repositorio para su despliegue.
release: sh -c 'python manage.py sqlflush | python manage.py dbshell && python manage.py makemigrations && python manage.py migrate'
web: sh -c 'gunicorn groovMind.wsgi --log-file -'
