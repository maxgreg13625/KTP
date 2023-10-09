import pytest
from src.utility import MY_AES

def test_my_aes_value_error():
    # act
    with pytest.raises(ValueError) as test_result:
         MY_AES('test', 20)
    # assert
    assert str(test_result.value) == "Invalid block size!!!"

def test_my_aes():
    key = 'test'
    aes = MY_AES(key)
    test_input = 'hello world'
    # act
    test_result = aes.encrypt(test_input)
    # assert
    assert test_input == aes.decrypt(test_result)