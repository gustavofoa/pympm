# pympm
#Novo site Músicas para Missa

##Requisitos para desenvolvimento
-Vagrant
-VirtualBox
-MySQL

###Iniciar máquina virtual
vagrant up

###Acessar a máquina virtual
vagrant ssh

###Executar a aplicação
sh /vagrant/script/runserver.sh

###Endereço da aplicação em dev
http://localhost:8000

##Enviar arquivos staticos para o S3
python manage.py collectstatic

##Deploy no Elastic Beanstalk
eb deploy
