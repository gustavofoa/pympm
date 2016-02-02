#!/usr/bin/env bash
# No vagrant é necessário especificar que a requisição poderá vir de qualquer lugar (inclusive do host)
cd /vagrant
python manage.py runserver [::]:8000
