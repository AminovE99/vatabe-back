python manage.py migrate --no-input
python manage.py collectstatic --no-input
apt-get update
apt-get install memcached
python manage.py createcachetable
# sh config/start_daphne.sh
python manage.py runserver 0.0.0.0:8000