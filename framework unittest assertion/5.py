import unittest
 
 
class Employee:
    """A simple class that describes an employee of the company."""
 
    TAX_RATE = 0.17
    BONUS_RATE = 0.10
 
    def __init__(
        self, first_name: str, last_name: str, salary: int
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
 
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
 
    @property
    def email(self) -> str:
        return (
            f'{self.first_name.lower()}.{self.last_name.lower()}'
            '@mail.com'
        )
 
    @property
    def tax(self) -> float:
        return round(self.salary * self.TAX_RATE, 2)
 
    def apply_bonus(self) -> None:
        self.salary = int(self.salary * (1 + self.BONUS_RATE))
 
 
class TestEmployee(unittest.TestCase):
    def test_has_email_attr(self) -> None:
        msg = 'The Employee class does not have an email attribute.'
        self.assertTrue(hasattr(Employee, 'email'), msg)
 
    def test_has_tax_attr(self) -> None:
        msg = 'The Employee class does not have a tax attribute.'
        self.assertTrue(hasattr(Employee, 'tax'), msg)
 
    def test_has_apply_bonus(self) -> None:
        msg = 'The Employee class does not have an apply_bonus attr.'
        self.assertTrue(hasattr(Employee, 'apply_bonus'), msg)


if __name__ == '__main__':
    unittest.main()