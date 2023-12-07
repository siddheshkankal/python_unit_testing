import unittest
from emp import Employee
 
 
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee('John', 'Smith', 40, 80000)
 
    def test_email(self):
        self.assertEqual(self.emp.email, 'john.smith@mail.com')