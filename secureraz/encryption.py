import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.db.models.fields import CharField
from django.conf import settings


"""
Setup the secret keys.
"""
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=settings.SECRET_KEY.encode(),
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(settings.ENCRYPTION_SECRET_KEY.encode()))
f = Fernet(key)


def encrypt(data):
    """
    Encrypt the field.
    :param data: Field to encrypt.
    :return: Encrypted field.
    """
    encrypted = f.encrypt(data.encode())
    return encrypted


def decrypt(data):
    """
    Decrypt the field.
    :param data: Field to decrypt.
    :return: Actual field(decrypted filed).
    """
    decrypted = f.decrypt(data).decode('utf-8')
    return decrypted


class Encryption(CharField):

    def get_prep_value(self, value):
        """ Encrypt the data when saving it into the database. """
        return encrypt(value)

    def from_db_value(self, value, expression, connection):
        """ Decrypt the data for display in Django as normal. """
        return decrypt(value)
