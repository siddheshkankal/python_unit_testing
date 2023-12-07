import unittest
from unittest.mock import patch
from employees import Programmer
 
 
class TestProgrammer(unittest.TestCase):
    def setUp(self):
        self.programmer = Programmer()
        self.programmer.add_tech('python') \
            .add_tech('sql') \
            .add_tech('java') \
            .add_tech('c++') \
            .add_tech('aws')
 
    @patch.object(Programmer, 'get_random_tech')
    def test_get_random_tech_mocked_python(self, mock_tech):
        mock_tech.return_value = 'python'
        result = self.programmer.get_random_tech()
        self.assertEqual(result, 'python')