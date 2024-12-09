import os.path

import yaml

from common.all_path import config_path


def load_yaml(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
        return data

config_path = os.path.join(config_path,'config.yml')

app_config = load_yaml(config_path)