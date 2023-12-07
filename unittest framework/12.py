import unittest
 
 
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
 
 
class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average_valid_input(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_average([2.5, 3.5, 4.5]), 3.5)
        self.assertEqual(calculate_average([-2, 0, 2]), 0)
 
    def test_calculate_average_empty_input(self):
        self.assertEqual(calculate_average([]), None)
 
    def test_calculate_average_invalid_input(self):
        self.assertRaises(TypeError, calculate_average, [1, 2, "3", 5])
        self.assertRaises(TypeError, calculate_average, ["a", "b", "c"])
        self.assertRaises(TypeError, calculate_average, [None, None])
        
        
if __name__ == '__main__':
    unittest.main()