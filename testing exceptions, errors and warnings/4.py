
import unittest
 
 
def find_longest_word(words):
    if not isinstance(words, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(word, str) for word in words):
        raise TypeError("List must contain only strings")
    if not words:
        raise ValueError("List cannot be empty")
    return max(words, key=len)
 
 
class TestFindLongestWord(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_longest_word([])
            
    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            find_longest_word(["apple", 5, "banana"])
        with self.assertRaises(TypeError):
            find_longest_word([True, False, None])
        with self.assertRaises(TypeError):
            find_longest_word(["hello", [1, 2, 3], "world"])



if __name__ == '__main__':
    unittest.main()