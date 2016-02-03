
#!/bin/sh
cd /var/projects/pympm && python manage.py migrate --noinput
supervisord -n -c /etc/supervisor/supervisord.conf
