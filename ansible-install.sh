#!/bin/bash
# Install required packages
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:ansible/ansible -y
sudo apt update
sudo apt install -y ansible