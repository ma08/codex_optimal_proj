#!/bin/bash

# set -x

# This script is used to run the application in a container
#
# The container uses the image created in the Dockerfile in the same directory
#
# ENV variables:
#
#   LISTEN_PORT - The port that the application will listen on
#
# Volumes:
#
#   /opt/app-root/src - Application source must be bind mounted into the container
#

set -e

# Source environment variables of the jenkins slave
# that might interest this worker. By default - nothing.
#if [ -e "jenkins-env" ]; then
#  cat jenkins-env | grep -E "(JENKINS_URL|GIT_BRANCH|GIT_COMMIT|BUILD_NUMBER|ghprbSourceBranch|ghprbActualCommit|BUILD_URL|ghprbPullId|ghprbTargetBranch|ghprbPullAuthorLogin|ghprbPullDescription)" >> /tmp/jenkins_env
#  source /tmp/jenkins_env
#fi

# We need to disable selinux for now, XXX
/usr/sbin/setenforce 0 || :

# Get all the deps in
yum -y install \
  docker \
  make \
  git \
  curl || :

# Install epel release
yum -y install epel-release || :

# Install ansible
yum -y install ansible || :

# Install python-pip
yum -y install python-pip || :

# Install docker-py via pip
pip install docker-py || :

# Install docker-compose via pip
pip install docker-compose || :

# Start docker
service docker start

# Install pip
#curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
#python get-pip.py

# Install docker-compose
#pip install docker-compose

# Build the application
#make build

# Run the application
#docker run -d -p ${LISTEN_PORT}:${LISTEN_PORT} --name=${APP_NAME} ${IMAGE_NAME}

# Start docker
#service docker start

# Install pip
#curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
#python get-pip.py

# Install docker-compose
#pip install docker-compose

# Build the application
#make build

# Run the application
#docker run -d -p ${LISTEN_PORT}:${LISTEN_PORT} --name=${APP_NAME} ${IMAGE_NAME}
