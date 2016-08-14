#!/usr/bin/env bash
 
if [ $(dpkg-query -W -f='${Status}' ansible 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
    echo "Add APT repositories"
    export DEBIAN_FRONTEND=noninteractive
    echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list
    apt-get update -qq
 
    echo "Installing Ansible"
    apt-get install -y -qq -t jessie-backports ansible python-psycopg2 &> /dev/null || exit 1
    echo "Ansible installed"
fi
 
cd /vagrant
ansible-playbook -i "localhost," -c local playbook.yml
