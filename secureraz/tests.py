from django.test import TestCase

from secureraz import encryption


class MyTestCase(TestCase):
    def test_decrypt_encrypt(self):
        """
        Test that the decrypted of an encrypted message
        matches the original value.
        """
        password = "my-fake-password"
        encrypted = encryption.encrypt(password)
        decrypted = encryption.decrypt(encrypted)
        self.assertEqual(decrypted, password)
