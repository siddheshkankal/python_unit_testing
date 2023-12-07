def is_palindrome(string: str) -> bool:
    """
    Determines whether the given string is a palindrome.
 
    :param string: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    string = string.lower().replace(" ", "")
    return string == string[::-1]
 
 
def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("not a palindrome") == False
 
 
if __name__ == '__main__':
    test_is_palindrome()