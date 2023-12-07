import unittest
 
 
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b
 
 
class TestAddNumbers(unittest.TestCase):
    """Tests for the `add_numbers` function."""
 
    def test_add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
 
    def test_add_negative_numbers(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)
 
    def test_add_zero(self):
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)
