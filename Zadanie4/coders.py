from cryptography.fernet import Fernet

class SymmetricCoders():
        
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(key)
    
    @staticmethod
    def GenerateKey():
        key = Fernet.generate_key()
        fernet = Fernet(key)
        return fernet

    def Encoder(message):
        token = SymmetricCoders.GenerateKey().encrypt(bytes(message, 'utf-8'))
        return token
    
    def Decoder(message):
        token = SymmetricCoders.generateKey().decrypt()
        return token
