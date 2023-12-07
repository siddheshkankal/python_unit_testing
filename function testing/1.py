import unittest
import math
 
 
def circle_area(radius):
    """Calculate the area of a circle given its radius."""
 
    if not isinstance(radius, (int, float)):
        raise TypeError('Radius must be of type int or float.')
 
    if not radius > 0:
        raise ValueError('Radius must be positive.')
 
    return math.pi * radius ** 2
 
 
class TestCircleArea(unittest.TestCase):
    def test_area_with_radius_one(self):
        self.assertAlmostEqual(circle_area(1), 3.14159, 5)
 
    def test_area_with_radius_three(self):
        self.assertAlmostEqual(circle_area(3), 28.27433, 5)
 
    def test_incorrect_type(self):
        self.assertRaises(TypeError, circle_area, '4')
        self.assertRaises(TypeError, circle_area, None)
 
    def test_incorrect_value(self):
        self.assertRaises(ValueError, circle_area, 0)
        self.assertRaises(ValueError, circle_area, -3)