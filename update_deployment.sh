git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
# gunicorn's --reload flag takes care of the rest
