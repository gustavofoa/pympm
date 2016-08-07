#!/usr/bin/env bash
# No vagrant é necessário especificar que a requisição poderá vir de qualquer lugar (inclusive do host)
cd /vagrant
virtualenv -p python3 pympm
cd pympm
source bin/activate
pip install -r /vagrant/requirements.txt
pip install awsebcli
cd /vagrant
python manage.py runserver [::]:8000
