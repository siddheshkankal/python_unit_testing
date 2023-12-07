
import unittest
 
 
def count_lines(filename: str) -> int:
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File {filename} not found") from e
 
 
class TestCountLines(unittest.TestCase):
    def test_count_lines_of_existing_file(self) -> None:
        self.assertEqual(count_lines('evaluate.py'), 21)
 
    def test_count_lines_of_non_existing_file(self) -> None:
        with self.assertRaises(FileNotFoundError):
            count_lines('non_existing_script.py')


if __name__ == '__main__':
    unittest.main()
    