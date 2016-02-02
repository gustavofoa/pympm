#!/usr/bin/env bash


sudo apt-get install linux-image-extra-$(uname -r) software-properties-common

sudo sh -c "wget -qO- https://get.docker.io/gpg | apt-key add -"

sudo sh -c "echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list"

sudo apt-get update

sudo apt-get -y install lxc-docker

sudo docker pull ubuntu
