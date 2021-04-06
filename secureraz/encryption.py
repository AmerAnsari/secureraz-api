from cryptography.fernet import Fernet
from django.conf import settings
from django.db.models.fields import CharField

# Get a Fernet instance with secret key.
f = Fernet(settings.ENCRYPTION_SECRET_KEY.encode())


def encrypt(data):
    """
    Encrypt the field.
    :param data: Field to encrypt.
    :return: Encrypted field.
    """
    return f.encrypt(data.encode())


def decrypt(data):
    """
    Decrypt the field.
    :param data: Field to decrypt.
    :return: Actual field(decrypted filed).
    """
    return f.decrypt(bytes(data, 'utf-8')).decode('utf-8')


class Encryption(CharField):

    def get_prep_value(self, value):
        """ Encrypt the data when saving it into the database. """
        return encrypt(value)

    def from_db_value(self, value, expression, connection):
        """ Decrypt the data for display in Django as normal. """
        return decrypt(value)
