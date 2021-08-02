export $(cat .server | xargs)
. env/bin/activate
python ../manage.py runserver $HOST:$PORT