import os
import yaml

config_path = os.environ.get('CONFIG_PATH')
if config_path is None:
    config_path = os.path.abspath(os.getcwd())

config_file = os.path.join(config_path, "config.yml")
config = {}

with open(config_file, 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print("Config Error:",exc)