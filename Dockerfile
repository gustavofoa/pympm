FROM python:latest
MAINTAINER Gustavo (gustavo.foa@gmail.com)

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
# Install python and npm
##############################################################################

RUN sudo apt-get install -y python-software-properties
RUN sudo apt-get -y install -y openssh-server vim git zip bzip2 fontconfig curl make
RUN sudo apt-get -y install python-pip
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install npm
RUN sudo npm install -g less

####################################################
# setup startup script for gunicord WSGI service
####################################################
RUN groupadd webapps
RUN useradd webapp -G webapps
RUN mkdir -p /var/log/webapp/ && chown -R webapp /var/log/webapp/ && chmod -R u+rX /var/log/webapp/
RUN mkdir -p /var/run/webapp/ && chown -R webapp /var/run/webapp/ && chmod -R u+rX /var/run/webapp/
####################################################
# Install and configure supervisord
####################################################
RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
ADD ./deploy/supervisor_conf.d/webapp.conf /etc/supervisor/conf.d/webapp.conf

####################################################
# Install dependencies and run scripts.
####################################################

RUN mkdir /var/projects/pympm
WORKDIR /var/projects/pympm
ADD requirements.txt /var/projects/pympm/
RUN pip install -r /var/projects/pympm/requirements.txt
ADD . /var/projects/pympm/

CMD ["sh", "./scripts/container_start.sh"]

EXPOSE 8002
