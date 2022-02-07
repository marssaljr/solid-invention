DATABASE=test coverage run --omit=*/venv/*,*/migrations/*,manage.py,*/config/* --source='.' manage.py test &&
coverage html
