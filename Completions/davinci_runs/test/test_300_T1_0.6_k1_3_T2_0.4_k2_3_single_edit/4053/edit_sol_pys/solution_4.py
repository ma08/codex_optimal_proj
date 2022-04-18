#!/bin/bash

# this script is used to fix syntax errors in files

# exit on error
set -e

# display commands
set -x

# go to root
cd

# install dependencies
apt-get install -y git

# clone the repository
git clone https://github.com/c9/core.git c9sdk

# go into the repository
cd c9sdk

# start the server
scripts/install-sdk.sh

# fix syntax errors
sed -i -e 's|127.0.0.1|0.0.0.0|g' ./configs/standalone.js 

# create a startup script
echo "node server.js -l 0.0.0.0 -a : -w ~/workspace" > cloud9

# make the file executable
chmod +x cloud9

# move the startup script to /etc/init.d
sudo mv cloud9 /etc/init.d

# start the server
sudo service cloud9 start
