from models.message import Message
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class Symmetric:

    def __init__(self):
        self.key = None

    @staticmethod
    def generateKey():
        """Method generating symmetric key.

        Returns:
            str: Symmetric key.
        """
        return Fernet.generate_key().hex()

    def setKey(self, givenKey: hex) -> None:
       self.key = Fernet(bytearray.fromhex(givenKey))

    def encode(self, message: str) -> bytes:
        """Method encoding given message.

        Args:
            message (str): Given message to encode.

        Returns:
            bytes: Encoded message.
        """
        encoded = self.key.encrypt(bytes(message, "utf-8"))
        return encoded

    def decode(self, message: str) -> bytes:
        """Method decoding encoded message.

        Args:
            message (str): Given encoded message to decode.

        Returns:
            bytes: Decoded message.
        """
        decoded = self.key.decrypt(bytes(message, "utf-8"))
        return decoded

class Asymmetric:

    def __init__(self):
        self.privateKey = None
        self.publicKey = None

    def generateKeys(self):
        basic = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        private_key = basic.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).hex()
        
        public_key = basic.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).hex()

        keys = [private_key, public_key]
        return keys

    def setKeys(self, keys):
        self.privateKey = keys[0]
        self.publicKey = keys[1]

    def generateSshKeys(self):
        basic = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        privateSshKey = basic.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        ).hex()

        publicSshKey = basic.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        ).hex()

        sshKeys = [privateSshKey, publicSshKey]
        return sshKeys


    

