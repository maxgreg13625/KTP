from src.utility import *

def test_get_config():
    config = get_config()
    assert 'Required' in config.sections()

    config = get_config('test.int')
    assert 'Required' in config.sections()