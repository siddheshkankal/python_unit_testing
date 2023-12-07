
import unittest
 
 
def calculate_area(length, width):
    if not isinstance(length, (int, float)):
        raise TypeError("Length must be a number")
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a number")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    return length * width
 
 
class TestCalculateArea(unittest.TestCase):
    def test_zero_values(self):
        with self.assertRaises(ValueError):
            calculate_area(0, 4)
        with self.assertRaises(ValueError):
            calculate_area(2, 0)
        with self.assertRaises(ValueError):
            calculate_area(0, 0)
            
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_area(-2, 4)
        with self.assertRaises(ValueError):
            calculate_area(2, -4)
        with self.assertRaises(ValueError):
            calculate_area(-2, -4)
    
    def test_non_number_values(self):
        with self.assertRaises(TypeError):
            calculate_area("two", 4)
        with self.assertRaises(TypeError):
            calculate_area(2, "four")
        with self.assertRaises(TypeError):
            calculate_area("two", "four")


if __name__ == '__main__':
    unittest.main()