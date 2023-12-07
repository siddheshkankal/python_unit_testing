
import unittest
 
 
def calculate_grade(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list")
    if not scores:
        raise ValueError("List cannot be empty")
    if not all(isinstance(score, (int, float)) for score in scores):
        raise TypeError("Elements of list must be numbers")
    if not all(0 <= score <= 100 for score in scores):
        raise ValueError("Elements of list must be between 0 and 100")
    return sum(scores) / len(scores)
 
 
class TestCalculateGrade(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(
            calculate_grade([90, 80, 70, 60]), 75.0, places=2
        )
        self.assertAlmostEqual(
            calculate_grade([100, 90, 80, 70]), 85.0, places=2
        )
        self.assertAlmostEqual(
            calculate_grade([50, 60, 70, 80]), 65.0, places=2
        )
        self.assertAlmostEqual(
            calculate_grade([85, 75, 95, 80, 70]), 81.0, places=2
        )
        self.assertAlmostEqual(
            calculate_grade([60, 80, 75, 70]), 71.25, places=2
        )
        self.assertAlmostEqual(
            calculate_grade([100, 90]), 95.0, places=2
        )




if __name__ == '__main__':
    unittest.main()
    
    