#!/bin/sh

apt-get install --reinstall libpq-dev
python3 -m pip install psycopg2
python3 -m pip install requests
python3 -m pip install twilio
python3 -m pip install selenium
pip install django-environ

chmod 0755 geckodriver  
cp geckodriver   /usr/local/bin/

python3 manage.py migrate
python3 manage.py createsuperuser

