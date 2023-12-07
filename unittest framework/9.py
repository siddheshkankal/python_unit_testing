import unittest
 
 
class StringReverser:
    def reverse(self, string):
        return string[::-1]
 
 
class TestStringReverser(unittest.TestCase):
    def test_reverse(self):
        # Create a new instance of the StringReverser class
        reverser = StringReverser()
 
        # Test that "hello" reversed is "olleh"
        self.assertEqual(reverser.reverse("hello"), "olleh")
 
        # Test that "12345" reversed is "54321"
        self.assertEqual(reverser.reverse("12345"), "54321")
 
        # Test that "" (empty string) reversed is ""
        self.assertEqual(reverser.reverse(""), "")


if __name__ == '__main__':
    unittest.main()