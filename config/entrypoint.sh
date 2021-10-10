python manage.py migrate --no-input
python manage.py collectstatic --no-input
apt-get update
python manage.py runserver 0.0.0.0:8000