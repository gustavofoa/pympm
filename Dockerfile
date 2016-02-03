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
# Install dependences
##############################################################################

RUN sudo apt-get install -y python-software-properties
RUN sudo apt-get -y install -y openssh-server vim git zip bzip2 fontconfig curl make
RUN sudo apt-get -y install python-pip
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install npm
RUN sudo npm install -g less

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

#CMD ["sh", "./scripts/container_start.sh"]

EXPOSE 80 8000
