import unittest
import subprocess

import password_compat

class TestComparePhp(unittest.TestCase):
    def test_php_password_hash(self):
        passwords = [
            "foo", "bar", "baz", "hoge", "fuga"
        ]

        for password in passwords:
            result = subprocess.run(["php", "php/password_hash.php", password], text=True, check=True, stdout=subprocess.PIPE)
            hashed_password = str(result.stdout).strip()

            self.assertTrue(password_compat.password_verify(password, hashed_password))


    def test_php_password_verify(self):
        passwords = [
            "foo", "bar", "baz", "hoge", "fuga"
        ]

        for password in passwords:
            hashed_password = password_compat.password_hash(password)

            result = subprocess.run(["php", "php/password_verify.php", password, hashed_password], check=True)
            self.assertEqual(result.returncode, 0)

