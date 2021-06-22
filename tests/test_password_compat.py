import unittest

import password_compat


class TestPasswordCompat(unittest.TestCase):
    def test_password_compat(self):
        passwords = [
            "foo", "bar", "baz", "hoge", "fuga"
        ]
        for password in passwords:
            hash = password_compat.password_hash(password)
            self.assertTrue(password_compat.password_verify(password, hash))
