import unittest
 
 
def calculate_bmi(height, weight):
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive")
    bmi = weight / (height ** 2)
    return bmi
 
 
class TestCalculateBMI(unittest.TestCase):
    def test_calculate_bmi_normal(self):
        result = calculate_bmi(1.7, 65)
        self.assertAlmostEqual(result, 22.49, delta=0.01)
 
    def test_calculate_bmi_invalid_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi(1.7, -50)
 
    def test_calculate_bmi_invalid_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(-1.7, 65)
1