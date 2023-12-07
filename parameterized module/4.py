import unittest
from parameterized import parameterized
 
 
class TestAverage(unittest.TestCase):
    @parameterized.expand(
        [
            ([1, 2, 3], 2),
            ([10, 20, 30, 40], 25),
            ([5], 5),
            ([0, 0, 0], 0),
            ([], None),
            (["not a number"], None),
            (["1", 2, 3], None),
            ([None], None),
        ]
    )
    def test_average(self, input_list, expected_output):
        if expected_output is None:
            with self.assertRaises((TypeError, ValueError)):
                average(input_list)
        else:
            self.assertEqual(average(input_list), expected_output)


For each test case, we use an if statement to check if the expected output is None. If it is, we use the assertRaises method with a tuple of exceptions to check that the function raises either a TypeError or ValueError. If it is not None, we use the assertEqual method to check that the function returns the correct average.