
import unittest
 
 
class StringListOnly(list):
    def append(self, string: str) -> None:
        if not isinstance(string, str):
            raise TypeError(
                'Only object of type str can be added to the list.'
            )
        super().append(string)
 
 
class TestStringListOnly(unittest.TestCase):
    def test_append_string(self) -> None:
        slo = StringListOnly()
        string = 'big_data'
        slo.append(string)
        self.assertIn(string, slo)
 
    def test_append_not_string_should_raise_error(self) -> None:
        slo = StringListOnly()
        not_string_1 = ['big_data']
        not_string_2 = True
        with self.assertRaises(TypeError):
            slo.append(not_string_1)
        with self.assertRaises(TypeError):
            slo.append(not_string_2)

if __name__ == '__main__':
    unittest.main()