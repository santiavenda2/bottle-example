#!/usr/bin/env bash
 
apt-get update
apt-get install -y apache2 apache2.2-common apache2-mpm-prefork apache2-utils libexpat1
apt-get install libapache2-mod-wsgi
service apache2 restart

apt-get install -y python-pip python-dev build-essential
pip install virtualenv

rm /etc/apache2/sites-enabled/*
cp -f /var/www/bottle-example.com/bottle-example.com.config /etc/apache2/sites-available/bottle-example.com
a2ensite bottle-example.com

cd /var/www/bottle-example.com

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

service apache2 reload

apt-get install screen