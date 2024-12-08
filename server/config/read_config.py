import yaml

from common.all_path import config_path


def load_yaml(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
        return data

config_path = config_path

app_config = load_yaml('config.yaml')