git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py crontab remove
python manage.py crontab add
python manage.py collectstatic --noinput
python manage.py loaddata anthill/fixtures/PostalcodeCoordinates.json
# gunicorn's --reload flag takes care of the rest
