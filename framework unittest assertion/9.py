import unittest
 
 
class Calculator:
    def divide(self, dividend: float, divisor: float) -> float:
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor
 
 
class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
 
    def test_divide_positive_numbers(self) -> None:
        cal = Calculator()
        self.assertEqual(cal.divide(10, 2), 5)
 
    def test_divide_zero_by_positive_number(self) -> None:
        self.assertEqual(self.calculator.divide(0, 5), 0)
 
    def test_divide_negative_by_positive_number(self) -> None:
        self.assertEqual(self.calculator.divide(-10, 2), -5)
 
    def test_divide_by_zero_should_raise_error(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)
    
    def tearDown(self) -> None:
        del self.calculator
        
if __name__ == '__main__':
    unittest.main()