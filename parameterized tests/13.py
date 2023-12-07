import unittest
 
 
def reverse_dict(input_dict):
    if not isinstance(input_dict, dict):
        raise TypeError("Input must be a dictionary")
    for key, value in input_dict.items():
        if not isinstance(value, int):
            raise ValueError("All values must be integers")
    return {value: key for key, value in input_dict.items()}
 
 
class TestReverseDict(unittest.TestCase):
    def test_reverse_dict(self):
        test_cases = [
            {
                "input": {"one": 1, "two": 2, "three": 3},
                "expected_output": {1: "one", 2: "two", 3: "three"},
            },
            {
                "input": {"a": 0, "b": -1, "c": 10},
                "expected_output": {0: "a", -1: "b", 10: "c"},
            },
            {"input": {}, "expected_output": {}},
            {
                "input": {"one": "1", "two": 2, "three": 3},
                "expected_output": None,
            },
            {
                "input": ["not a dictionary"],
                "expected_output": None,
            },
            {
                "input": {"one": 1, "two": "2", "three": 3},
                "expected_output": None,
            },
            {
                "input": {"one": 1, "two": 2, "three": "3"},
                "expected_output": None,
            },
            {
                "input": {"one": 1, "two": 2, 3: "three"},
                "expected_output": None,
            },
        ]
 
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                if not isinstance(test_case["input"], dict):
                    self.assertRaises(
                        TypeError,
                        reverse_dict,
                        test_case["input"],
                    )
                elif not all(
                    isinstance(value, int)
                    for value in test_case["input"].values()
                ):
                    self.assertRaises(
                        ValueError,
                        reverse_dict,
                        test_case["input"],
                    )
                else:
                    self.assertEqual(
                        reverse_dict(test_case["input"]),
                        test_case["expected_output"],
                    )