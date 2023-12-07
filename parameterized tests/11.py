import unittest
 
 
def quotient(numbers):
    if numbers[1] == 0:
        raise ValueError('Division by zero')
    return numbers[0] / numbers[1]
 
 
class TestQuotient(unittest.TestCase):
    def test_quotient(self):
        test_cases = [
            {'input': [1, 2], 'expected_output': 0.5},
            {'input': [10, 5], 'expected_output': 2},
            {'input': [2, 0], 'expected_output': None},
            {'input': [-10, 5], 'expected_output': -2},
            {'input': [0, 1], 'expected_output': 0},
            {'input': [0, 0], 'expected_output': None}
        ]
        
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                if test_case["input"][1] == 0:
                    self.assertRaises(
                        ValueError, quotient, test_case["input"]
                    )
                else:
                    self.assertEqual(
                        quotient(test_case["input"]),
                        test_case["expected_output"],
                    )
