import unittest
 
 
class TestUpper(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('summer'.upper(), 'SUMMER')
 
    def test_is_upper(self):
        self.assertTrue('SUMMER'.isupper())
        self.assertFalse('summer'.isupper())
 
 
if __name__ == '__main__':
    unittest.main()