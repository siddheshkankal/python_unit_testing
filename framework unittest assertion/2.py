import unittest
 
 
def calculate_daily_return(
    open_price: float, close_price: float
) -> float:
    return round(((close_price / open_price) - 1) * 100, 7)
 
 
class TestCalculateDailyReturn(unittest.TestCase):
    def test_positive_return(self) -> None:
        self.assertAlmostEqual(
            calculate_daily_return(349, 360), 3.1518625
        )
 
    def test_negative_return(self) -> None:
        self.assertAlmostEqual(
            calculate_daily_return(349, 340), -2.5787966
        )
 
    def test_zero_return(self) -> None:
        self.assertAlmostEqual(
            calculate_daily_return(349.0, 349.0), 0.0
        )
        
        
if __name__ == '__main__':
    unittest.main()