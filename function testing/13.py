import random
import string
import unittest
 
 
def generate_password(n):
    password = ''.join(
        random.choices(
            string.ascii_uppercase
            + string.ascii_lowercase
            + string.digits,
            k=n,
        )
    )
    return password
 
 
class TestGeneratePassword(unittest.TestCase):
    def test_generate_password(self):
        result = generate_password(10)
        self.assertEqual(len(result), 10)
        self.assertTrue(any(c.isupper() for c in result))
        self.assertTrue(any(c.islower() for c in result))
        self.assertTrue(any(c.isdigit() for c in result))