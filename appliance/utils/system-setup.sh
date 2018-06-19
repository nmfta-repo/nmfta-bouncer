#!/bin/bash

echo "Run As Root"
echo "Firewall System Installer"
echo "Installing system packages"

apt install ufw python3-pip -y

pip3 install -r requirements.txt
