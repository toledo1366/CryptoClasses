import hashlib
import os


class AccountModel:
    """Data model class for keeping basic data structure"""

    def __init__(self, name, password):
        self.name = name
        self.salt = os.urandom(16)
        self.password = self.hashPassword(password, self.salt)

    def get_salt(self):
        return self.salt

    def get_password(self):
        return self.password

    def get_name(self):
        return self.name

    def hashPassword(self, password, salt):
        """Function hashing model's password"""

        key = hashlib.pbkdf2_hmac(
            'sha256',
            str.encode(password),
            salt,
            1000000
        )
        return key.hex()
