web: gunicorn config.wsgi:application
heroku ps:scale web=1
python manage.py collectstatic --noinput
manage.py migrate
