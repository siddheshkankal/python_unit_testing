import unittest
 
 
def string_lengths(strings):
    return list(map(len, strings))
 
 
class TestStringLengths(unittest.TestCase):
    def test_string_lengths(self):
        test_cases = [
            {
                "input": ["hello", "world"],
                "expected_output": [5, 5],
            },
            {
                "input": ["python", "is", "awesome"],
                "expected_output": [6, 2, 7],
            },
            {
                 "input": [], 
                 "expected_output": []
            },
            {
                "input": ["1", "22", "333", "4444"],
                "expected_output": [1, 2, 3, 4],
            },
        ]
 
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                input_strings = test_case["input"]
                expected_output = test_case["expected_output"]
                self.assertEqual(
                    string_lengths(input_strings),
                    expected_output,
                )
