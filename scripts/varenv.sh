#!/usr/bin/env bash
echo "Setting Environment Variables"

source /home/vagrant/.profile && [ -z "$DB_NAME" ] && echo 'export DB_NAME="pympm"' >> /home/vagrant/.profile
source /home/vagrant/.profile && [ -z "$DB_USER" ] && echo 'export DB_USER="pympm"' >> /home/vagrant/.profile
source /home/vagrant/.profile && [ -z "$DB_PASSWORD" ] && echo 'export DB_PASSWORD="pympm"' >> /home/vagrant/.profile
source /home/vagrant/.profile && [ -z "$DB_HOST" ] && echo 'export DB_HOST="$(netstat -rn | grep "^0.0.0.0 " | cut -d " " -f10)"' >> /home/vagrant/.profile
source /home/vagrant/.profile && [ -z "$DB_PORT" ] && echo 'export DB_PORT="3306"' >> /home/vagrant/.profile

echo "Done."
