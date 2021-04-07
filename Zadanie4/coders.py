from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives.serialization import load_pem_parameters

class SymmetricCoders():
        
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(key)
    
    @staticmethod
    def GenerateKey():
        key = Fernet.generate_key()
        return key

    def Encoder(self, message):
        token = self.fernet.encrypt(bytes(message, 'utf-8'))
        return token
    
    def Decoder(self, message):
        token = self.fernet.decrypt(bytes(message, 'utf-8'))
        return token

class AsymetricCoders():

    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(key)
    
    @staticmethod
    def GenerateKeys():
        private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
        )
        public_key = private_key.public_key()
        return {"Private key" : private_key, "Public key" : public_key}
    
    @staticmethod
    def generate_ssh_keys():
        return {"Private key" : 1, "Public key" : 1}
    

