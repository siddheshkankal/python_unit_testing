


import unittest
 
 
class Doc:
    def __init__(self, string: str) -> None:
        self.string = string
 
    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"
 
    def __eq__(self, other) -> bool:
        return len(self.string) == len(other.string)
 
    def __ne__(self, other) -> bool:
        return len(self.string) != len(other.string)
 
 
class TestDoc(unittest.TestCase):
    def test_equal(self) -> None:
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        self.assertEqual(doc1, doc2)
 
    def test_not_equal(self) -> None:
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        doc3 = Doc('Technology')
        self.assertNotEqual(doc3, doc1)
        self.assertNotEqual(doc3, doc2)



if __name__ == '__main__':
    unittest.main()