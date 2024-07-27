from src.utility import *
from configparser import ConfigParser

def test_get_config():
    config = get_config()
    assert 'Required' in config.sections()

    config = get_config('test.int')
    assert 'Required' in config.sections()

def test_export_config(mocker):
    mocker.patch('builtins.open')
    mocker.patch('configparser.ConfigParser.write')

    test_conifg = ConfigParser()
    test_conifg['test'] = {'test': 'test'}

    assert export_config(test_conifg)