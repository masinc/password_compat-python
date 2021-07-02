import unittest
import subprocess

import password_compat

class TestCompareOldPhp(unittest.TestCase):
    def test_php_password_hash(self):
        passwords = [
            "foo", "bar", "baz", "hoge", "fuga"
        ]

        for password in passwords:
            result = subprocess.run(["php", "old-php/password_hash.php", password], check=True, stdout=subprocess.PIPE)
            hashed_password: bytes = result.stdout
            hashed_password: str = hashed_password.decode().strip()

            self.assertTrue(password_compat.password_verify(password, hashed_password))


    def test_php_password_verify(self):
        passwords = [
            "foo", "bar", "baz", "hoge", "fuga"
        ]

        for password in passwords:
            hashed_password = password_compat.password_hash(password)

            result = subprocess.run(["php", "old-php/password_verify.php", password, hashed_password], check=True)
            self.assertEqual(result.returncode, 0)

