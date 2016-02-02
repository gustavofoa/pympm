FROM ubuntu:latest

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y

RUN sudo apt-get install -y python-software-properties
RUN sudo apt-get -y install -y openssh-server vim git zip bzip2 fontconfig curl make
RUN sudo apt-get -y install python-pip
RUN sudo apt-get -y install python-dev
RUN sudo pip install Django
RUN sudo pip install django-enumfield
RUN sudo apt-get -y install npm
RUN sudo npm install -g less

CMD ["sh", "./scripts/runserver.sh"]

EXPOSE 8000
