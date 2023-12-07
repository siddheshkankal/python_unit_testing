import unittest
from tax import SimpleTaxCalculator
 
 
class TestIncomeTax(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()
 
    def test_income_below_threshold(self):
        expected_tax = 10200
        actual_tax = self.calc.income_tax(60000)
        self.assertEqual(actual_tax, expected_tax)
 
    def test_income_equal_threshold(self):
        expected_tax = 14539.76
        actual_tax = self.calc.income_tax(85528)
        self.assertEqual(actual_tax, expected_tax)
 
    def test_income_above_threshold(self):
        expected_tax = 19170.8
        actual_tax = self.calc.income_tax(100000)
        self.assertEqual(actual_tax, expected_tax)
 
 
class TestVatTax(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()
        
    def test_vat_tax_with_zero_price(self):
        expected_tax = 0
        actual_tax = self.calc.vat_tax(0)
        self.assertEqual(actual_tax, expected_tax)
        
    def test_vat_tax_with_max_float_price(self):
        expected_tax = float('inf')
        actual_tax = self.calc.vat_tax(float('inf'))
        self.assertEqual(actual_tax, expected_tax)
        
    def test_vat_tax_with_string_input(self):
        with self.assertRaises(TypeError):
            self.calc.vat_tax('price')