import unittest
from bank_account import BankAccount
 
 
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("111", 1000, "checking")
        self.account2 = BankAccount("222", 500, "savings")
 
    def test_deposit(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.balance, 1500)
 
    def test_withdraw(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.balance, 500)
 
    def test_transfer(self):
        self.account1.transfer(500, self.account2)
        self.assertEqual(self.account1.balance, 500)
        self.assertEqual(self.account2.balance, 1000)
