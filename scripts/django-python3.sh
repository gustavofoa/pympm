#!/usr/bin/env bash

echo ">> Update repository"
sudo apt-get update

# need to be in first as it installs add-apt-repository command
echo ">> Install Python"
sudo apt-get install -y python-software-properties python-pip python-dev python3-dev

echo ">> Install utilities"
sudo apt-get -y install -y openssh-server vim git zip bzip2 fontconfig curl make tree git

echo ">> Install Virtualenv"
sudo pip install virtualenv

# echo ">> Install Mysql client"
# sudo apt-get -y install libmysqlclient-dev

echo ">> Install npm"
sudo apt-get -y install npm

echo ">> Install less"
sudo npm install -g less

echo ">> Done."
