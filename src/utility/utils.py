import os
from configparser import ConfigParser

def get_config(path: str='') -> ConfigParser:
    config = ConfigParser()
    if path == '':
        path = os.path.join(os.getcwd(), 'setting', 'config.ini')

    try:
        with open(path) as f:
            config.read_file(f)
    except:
        print(f"config file: {path} doesn't exist..")
        config['Required'] = {'test': 'test'}
    return config

def export_config(config: ConfigParser, path: str=''):
    if path == '':
        path = os.path.join(os.getcwd(), 'setting', 'encrypt_config.ini')

    # in order to keep config key in original case
    config.optionxform = lambda option: option

    with open(path, 'w') as configfile:
        config.write(configfile)
