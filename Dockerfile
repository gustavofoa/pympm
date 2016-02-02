FROM ubuntu:latest

##############################################################################
# Environment variables
##############################################################################
# Get noninteractive frontend for Debian to avoid some problems:
#    debconf: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y

##############################################################################
# Install and configure supervisord
##############################################################################

RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
ADD ./deploy/supervisor_conf.d/webapp.conf /etc/supervisor/conf.d/webapp.conf

##############################################################################
# Setup environment
##############################################################################

ADD .      /var/projects/project
WORKDIR /var/projects/project

##############################################################################
# Install dependences
##############################################################################

RUN sudo apt-get install -y python-software-properties
RUN sudo apt-get -y install -y openssh-server vim git zip bzip2 fontconfig curl make
RUN sudo apt-get -y install python-pip
RUN sudo apt-get -y install python-dev
RUN sudo pip install Django
RUN sudo pip install django-enumfield
RUN sudo apt-get -y install npm
RUN sudo npm install -g less

CMD ["sh", "./scripts/container_start.sh"]

EXPOSE 80
