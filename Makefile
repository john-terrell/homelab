all:
	ansible-galaxy install -r ./src/roles/requirements.yml
	ansible-playbook --ask-vault-pass src/site.yml -e@./src/vaulted_vars.yml -l hl8
