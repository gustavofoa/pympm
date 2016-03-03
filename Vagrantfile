
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://vagrantcloud.com/ubuntu/boxes/trusty64/versions/14.04/providers/virtualbox.box"
  config.vm.provision :shell, path: "scripts/django.sh"
  config.vm.provision :shell, path: "scripts/varenv.sh"
  # config.vm.provision :shell, inline: "source /vagrant/scripts/varenv.sh"
  config.vm.provision :shell, inline: 'echo "export VAR=value" >> /home/vagrant/.bashrc'

  # config.vm.provision :shell, path: "scripts/runserver.sh"
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  # VirtualBox Specific Customization
    config.vm.provider "virtualbox" do |vb|
    # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    end
#  config.vm.provider "docker" do |d|
#    d.build_dir = "."
#  end
end
