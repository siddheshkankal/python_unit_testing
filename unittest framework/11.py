import unittest
 
 
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32
 
 
class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self) -> None:
        c = TemperatureConverter()
        # Test that 0 degrees Celsius is 32 degrees Fahrenheit
        self.assertAlmostEqual(
            c.celsius_to_fahrenheit(0), 32, delta=0.5
        )
 
        # Test that 100 degrees Celsius is 212 degrees Fahrenheit
        self.assertAlmostEqual(
            c.celsius_to_fahrenheit(100), 212, delta=0.5
        )
 
        # Test that -40 degrees Celsius is -40 degrees Fahrenheit
        self.assertAlmostEqual(
            c.celsius_to_fahrenheit(-40), -40, delta=0.5
        )
        
        
if __name__ == '__main__':
    unittest.main()