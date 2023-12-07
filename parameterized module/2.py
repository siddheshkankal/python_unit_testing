import unittest
from parameterized import parameterized
 
 
def reverse_string(input_str):
    return input_str[::-1]
 
 
class TestReverseString(unittest.TestCase):
    @parameterized.expand([
        ("hello", "olleh"),
        ("python", "nohtyp"),
        ("racecar", "racecar"),
        ("12345", "54321"),
        ("", "")
    ])
    def test_reverse_string(self, input_str, expected_output):
        self.assertEqual(reverse_string(input_str), expected_output)