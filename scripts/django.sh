#!/usr/bin/env bash

echo ">> Update repository"
sudo apt-get update

# need to be in first as it installs add-apt-repository command
echo ">> Install Python"
sudo apt-get install -y python-software-properties

echo ">> Install utilities"
sudo apt-get -y install -y openssh-server vim git zip bzip2 fontconfig curl make

echo ">> Install Python-pip and Python-dev"
sudo apt-get -y install python-pip python-dev

echo ">> Install Requirements"
sudo pip install -r /vagrant/requirements.txt

echo ">> Install npm"
sudo apt-get -y install npm

echo ">> Install less"
sudo npm install -g less

echo ">> Install Python-mysqldb"
sudo apt-get -y install python-mysqldb

echo ">> Done."
