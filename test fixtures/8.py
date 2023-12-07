import unittest
import tempfile
 
 
class FileReader:
    def read_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()
 
 
class TestFileReader(unittest.TestCase):
    def setUp(self):
        # Create a new temporary file and write some data to it
        self.file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.file.write("Hello, world!")
        self.file.close()
 
    def tearDown(self):
        # Delete the temporary file
        import os
        os.unlink(self.file.name)
 
    def test_read_file(self):
        # Create a new instance of the FileReader class
        reader = FileReader()
 
        # Read the contents of the test file using the read_file method
        result = reader.read_file(self.file.name)
 
        # Check that the contents of the file match the expected value
        self.assertEqual(result, "Hello, world!")