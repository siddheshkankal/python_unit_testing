import unittest
 
 
class TestStartsWithMethod(unittest.TestCase):
    def test_startswith_one_letter(self):
        self.assertTrue('unittest'.startswith('u'))
        self.assertFalse('unittest'.startswith('U'))
 
    def test_startswith_four_letters(self):
        self.assertTrue('http://www.e-smartdata.org/'.startswith('http'))
        self.assertFalse('www.e-smartdata.org/'.startswith('http'))
 
 
class TestEndsWithMethod(unittest.TestCase):
 
    def test_endswith_three_letter(self):
        self.assertTrue('e-smartdata.org'.endswith('org'))
        self.assertFalse('e-smartdata.org'.endswith('com'))
 
 
if __name__ == '__main__':
    unittest.main()