python manage.py collectstatic --no-input && 
  echo "Iniciando servidor em modo produção"
  CACHE=main DATABASE=main gunicorn config.wsgi:application -c ./gunicorn.conf.py
