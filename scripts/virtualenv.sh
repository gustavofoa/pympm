#!/usr/bin/env bash
#Tem que copiar e colar no prompt
cd /vagrant
virtualenv -p python3 pympm
cd pympm
source bin/activate
pip install -r /vagrant/requirements.txt
pip install awsebcli
cd /vagrant
