DATABASE=test coverage run --omit=*/venv/*,*/migrations/*,manage.py --source='.' manage.py test &&
coverage html
