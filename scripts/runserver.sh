#!/usr/bin/env bash
# No vagrant é necessário especificar que a requisição poderá vir de qualquer lugar (inclusive do host)
python manage.py runserver [::]:9000
