import base64
from Crypto.Cipher import AES

class MY_AES:
    def __init__(self, key: str, bs: int=16):
        if bs % 16 != 0:
            raise ValueError("Invalid block size!!!")
        self.key = MY_AES._pad(key).encode()
        self._init_cipher()
        AES.block_size = bs

    def _init_cipher(self) -> None:
        self.cipher = AES.new(self.key, AES.MODE_ECB)
    
    def encrypt(self, input: str) -> str:
        input = MY_AES._pad(input)
        return base64.b64encode(self.cipher.encrypt(input.encode())).decode()

    def decrypt(self, input: str) -> str:
        input = base64.b64decode(input)
        return MY_AES._unpad(self.cipher.decrypt(input)).decode()

    @staticmethod
    def _pad(s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]