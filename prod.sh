python manage.py collectstatic --no-input && 
echo "Iniciando servidor em modo produção"
gunicorn config.wsgi:application -c ./gunicorn.conf.py
