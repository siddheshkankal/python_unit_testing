import unittest
 
 
class Calculator:
    def add(self, x, y):
        return x + y
 
    def subtract(self, x, y):
        return x - y
 
 
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
 
    def tearDown(self):
        del self.calculator
 
    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)
 
    def test_subtract(self):
        result = self.calculator.subtract(3, 2)
        self.assertEqual(result, 1)