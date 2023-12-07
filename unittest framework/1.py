import unittest
 
# expected = ['summer', 'time', 'vibes']
class TestSplitMethod(unittest.TestCase):
    
    def test_split_by_default(self):
        self.assertEqual('Python Testing'.split(), ['Python', 'Testing'])
 
    def test_split_by_comma(self):
        actual = 'open,high,low,close'.split(',')
        expected = ['open', 'high', 'low', 'close']
        self.assertEqual(actual, expected)
 
    def test_split_by_hash(self):
        actual = 'summer#time#vibes'.split('#')
        expected = ['summer', 'time', 'vibes']
        self.assertEqual(actual, expected)
 
 
if __name__ == '__main__':
    unittest.main()
