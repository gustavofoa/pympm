
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://vagrantcloud.com/ubuntu/boxes/trusty64/versions/14.04/providers/virtualbox.box"
  config.vm.provision :shell, path: "scripts/django.sh"
  config.vm.provision :shell, path: "scripts/varenv.sh"
  config.vm.provision :shell, inline: 'echo "export VAR=value" >> /home/vagrant/.bashrc'

  # config.vm.provision :shell, path: "scripts/runserver.sh"
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.network :forwarded_port, guest: 8001, host: 8001
    config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    end
end
