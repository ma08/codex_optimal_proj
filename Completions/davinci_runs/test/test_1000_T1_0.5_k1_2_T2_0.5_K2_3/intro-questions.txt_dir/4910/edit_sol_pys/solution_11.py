#!/bin/bash

# install the git
if [ ! -f /usr/bin/git ]; then
	yum -y install git
fi

if [ ! -f /usr/bin/docker ]; then
	yum -y install docker
fi

# pull the docker image
if [ ! -f /usr/bin/docker ]; then
	docker pull ubuntu
fi

# pull the git repo
if [ ! -d /home/vagrant/ubuntu ]; then
	git clone https://github.com/mrajput/ubuntu.git /home/vagrant/ubuntu
fi

# build the docker image
if [ ! -d /home/vagrant/ubuntu/ubuntu ]; then
	docker build -t ubuntu /home/vagrant/ubuntu/ubuntu
fi

# run the docker container
docker run -itd --name ubuntu ubuntu
