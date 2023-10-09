import os
from configparser import ConfigParser

def get_config(path: str='') -> ConfigParser:
    config = ConfigParser()
    if path == '':
        path = os.path.join(os.getcwd(), 'setting', 'config.ini')
 
    config.read(path)
    return config