#!/usr/bin/python3
import json
import sys

result = {}
rewrite_daemon_json = False
daemon_json_path = '/etc/docker/daemon.json'

try:
    with open(daemon_json_path, 'r') as fp:
        daemon_config = json.load(fp)

except IOError:
    daemon_config = {}
    daemon_config['data-root'] = '/var/lib/docker'
    result['new_config'] = True

# Requested new data root passed as first argument.
new_data_root = sys.argv[1]

old_data_root = daemon_config['data-root']

if (old_data_root != new_data_root):
    daemon_config['data-root'] = new_data_root
    rewrite_daemon_json = True

    if (old_data_root.endswith('/') == False):
        old_data_root += "/"

    result['changed'] = True
    result['old_data_root'] = old_data_root
else:
    result['changed'] = False

if (rewrite_daemon_json):
    with open(daemon_json_path, 'w', encoding='utf-8') as f:
        json.dump(daemon_config, f, ensure_ascii=False, indent=4)

print(json.dumps(result, indent=4))
