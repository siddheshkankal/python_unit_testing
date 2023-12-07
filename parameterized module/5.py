import unittest
from parameterized import parameterized
 
 
class TestSortStrings(unittest.TestCase):
    @parameterized.expand(
        [
            (["hello", "world"], ["hello", "world"]),
            (["z", "a", "c"], ["a", "c", "z"]),
            ([], []),
            (["hello", 123], None),
            ({"not": "a list"}, None),
            (["hello", None], None),
        ]
    )
    def test_sort_strings(self, input_list, expected_output):
        if expected_output is None:
            with self.assertRaises((TypeError, ValueError)):
                sort_strings(input_list)
        else:
            self.assertEqual(sort_strings(input_list), expected_output)


For each test case, we use an if statement to check if the expected output is None. If it is, we use the assertRaises method with a tuple of exceptions to check that the function raises either a TypeError or ValueError. If it is not None, we use the assertEqual method to check that the function returns the correct sorted list.