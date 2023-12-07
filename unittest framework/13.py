import unittest
 
 
def find_largest(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers")
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
 
 
class TestFindLargest(unittest.TestCase):
    def test_find_largest_valid_input(self):
        self.assertEqual(find_largest([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_largest([2, -3, 4, 0, -1]), 4)
        self.assertEqual(find_largest([-2, -5, -3]), -2)
 
    def test_find_largest_empty_input(self):
        self.assertEqual(find_largest([]), None)
 
    def test_find_largest_invalid_input(self):
        self.assertRaises(TypeError, find_largest, [1, 2, "3", 4, 5])
        self.assertRaises(TypeError, find_largest, ["a", "b", "c"])
        self.assertRaises(TypeError, find_largest, [None, True])
        
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    