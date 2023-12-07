import unittest
 
 
def sum_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 1)
 
 
class TestSumOddNumbers(unittest.TestCase):
    def test_sum_odd_numbers(self):
        test_cases = [
            {'input': [1, 2, 3, 4, 5], 'expected_output': 9},
            {'input': [10, 11, 12, 13, 14, 15], 'expected_output': 39},
            {'input': [2, 4, 6], 'expected_output': 0},
            {'input': [], 'expected_output': 0},
            {'input': [1, 3, 5, 7], 'expected_output': 16}
        ]
        
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                input_numbers = test_case['input']
                expected_output = test_case['expected_output']
                self.assertEqual(
                    sum_odd_numbers(input_numbers), expected_output
                )
