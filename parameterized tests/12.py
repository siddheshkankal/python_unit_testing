import unittest
 
 
def remove_vowels(input_str):
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    vowels = ["a", "e", "i", "o", "u"]
    return "".join(
        [char for char in input_str if char.lower() not in vowels]
    )
 
 
class TestRemoveVowels(unittest.TestCase):
    def test_remove_vowels(self):
        test_cases = [
            {
                "input": "hello world",
                "expected_output": "hll wrld",
            },
            {
                "input": "Python is awesome",
                "expected_output": "Pythn s wsm",
            },
            {
                "input": "aeiou",
                "expected_output": "",
            },
            {
                "input": "",
                "expected_output": "",
            },
            {
                "input": ["not a string"],
                "expected_output": None,
            },
            {
                "input": {
                    "not a string": "value"
                },
                "expected_output": None,
            },
            {
                "input": None,
                "expected_output": None,
            },
        ]
 
        
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                if not isinstance(test_case["input"], str):
                    self.assertRaises(
                        TypeError,
                        remove_vowels,
                        test_case["input"],
                    )
                else:
                    self.assertEqual(
                        remove_vowels(test_case["input"]),
                        test_case["expected_output"],
                    )
