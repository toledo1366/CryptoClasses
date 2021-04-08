from models.message import Message
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import base64
from cryptography.exceptions import InvalidSignature

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

    def generateKeys(self)->None:
        """Generate public and private keys.
        """
        self.privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        self.publicKey = self.privateKey.public_key()

    def setKeys(self, privKey, pubKey):
        self.privateKey = serialization.load_pem_private_key(bytearray.fromhex(privKey), password=None)
        self.publicKey = serialization.load_pem_public_key(bytearray.fromhex(pubKey))

    def getHex(self)->list:
        """Gets list of hex keys.

        Returns:
            list: List of hex keys.
        """
        privHex = self.privateKey.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()).hex()
        pubHex = self.privateKey.public_key().public_bytes(encoding=serialization.Encoding.PEM, format = serialization.PublicFormat.SubjectPublicKeyInfo).hex()
        hexes = []
        hexes.append(privHex)
        hexes.append(pubHex)
        return hexes

    def getSsh(self)->list:
        """Gets list of SSH keys.

        Returns:
            list: List of SSH keys.
        """
        privateSsh = self.privateKey.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.OpenSSH, encryption_algorithm=serialization.NoEncryption()).hex()
        publicSsh = self.privateKey.public_key().public_bytes(encoding=serialization.Encoding.OpenSSH, format=serialization.PublicFormat.OpenSSH).hex()
        ssh_keys = []
        ssh_keys.append(privateSsh)
        ssh_keys.append(publicSsh)
        return ssh_keys

    def signMessage(self, message:str)->bytes:
        """Signing message using private key.

        Args:
            message (str): Raw message content.

        Returns:
            bytes: Signed message.
        """
        signedMessage = base64.b64encode(self.privateKey.sign(
                bytes(message, "utf-8"),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        )
        return signedMessage

    def verifyMessage(self, message:str, sign:str)->bool:
        """Verify if message was signed right.

        Args:
            message (str): Raw message.
            sign (str): Signed message.

        Returns:
            bool: Response if message was signed correctly.
        """
        decoded = base64.b64encode(bytes(sign, "utf-8"))
        try:
            self.publicKey.verify(
                decoded, 
                bytes(message, "utf-8"),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            ) 
            return True
        except InvalidSignature:
            return False

    def encode(self, messageToEncode:str)->bytes:
        """Encoding raw message

        Args:
            messageToEncode (str): Raw message.

        Returns:
            bytes: Encoded message.
        """
        encodedMessage = base64.b64encode(self.publicKey.encrypt(
            bytes(messageToEncode, "utf-8"),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ))
        return encodedMessage

    def decode(self, messageToDecode:str)->str:
        """Decoding message.

        Args:
            messageToDecode (str): Encoded message.

        Returns:
            str: Decoded message.
        """
        decodedMessage = self.privateKey.decrypt(
            base64.b64encode(bytes(messageToDecode, "utf-8")),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA384()),
                algorithm=hashes.SHA384(),
                label=None
            )
        )