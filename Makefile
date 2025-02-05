all:
	ansible-galaxy install -r ./src/roles/requirements.yml
	ansible-playbook --ask-become-pass src/site.yml
