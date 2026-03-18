import unittest
# bank_account.py

class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds")
        self.balance -= amount

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Other account must be a BankAccount instance")
        self.withdraw(amount)
        other_account.deposit(amount)

    def get_balance(self):
        return self.balance

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)
        self.other_account = BankAccount(0)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw_success(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60)

    def test_withdraw_insufficient(self):
        with self.assertRaises(InsufficientFunds):
            self.account.withdraw(200)

    def test_transfer(self):
        self.account.transfer(self.other_account, 50)
        self.assertEqual(self.account.get_balance(), 50)
        self.assertEqual(self.other_account.get_balance(), 50)

    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

if __name__ == '__main__':
    unittest.main()