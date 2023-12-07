import unittest
from parameterized import parameterized
 
 
def square_pairs(numbers):
    return [(x, x**2) for x in numbers]
 
 
class TestSquarePairs(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4, 5], [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]),
        ([-1, 0, 1], [(-1, 1), (0, 0), (1, 1)]),
        ([], []),
        ([2**31-1], [(2**31-1, (2**31-1)**2)])
    ])
    def test_square_pairs(self, input_list, expected_output):
        self.assertEqual(square_pairs(input_list), expected_output)
