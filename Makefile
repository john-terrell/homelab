all:
	ansible-galaxy install -r ./src/roles/requirements.yml
	ansible-playbook -i src/inventories/ src/playbook.yml

network:
	ansible-galaxy install -r ./src/roles/requirements.yml 
	ansible-playbook -i src/inventories/01-network/hosts.yml src/site.yml

services:
	ansible-galaxy install -r ./src/roles/requirements.yml 
	ansible-playbook -i src/inventories/05-services/hosts.yml src/site.yml
