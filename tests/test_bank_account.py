"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Common valid BankAccount instance for reuse
        self.account = BankAccount(20019, 1010, 6764.67)

    def test_valid_initialization(self):
        self.assertEqual(
            self.account._BankAccount__account_number, 20019
        )
        self.assertEqual(
            self.account._BankAccount__client_number, 1010
        )
        self.assertEqual(
            round(self.account._BankAccount__balance, 2), 6764.67
        )

    def test_invalid_account_number_type(self):
        with self.assertRaises(ValueError):
            BankAccount("20019", 1010, 100.0)

    def test_invalid_client_number_type(self):
        with self.assertRaises(ValueError):
            BankAccount(20019, "1010", 100.0)

    def test_invalid_balance_type_sets_zero(self):
        account = BankAccount(20019, 1010, "not-a-number")
        self.assertEqual(
            round(account._BankAccount__balance, 2), 0.0
        )

    def test_account_number_property(self):
        self.assertEqual(self.account.account_number, 20019)

    def test_client_number_property(self):
        self.assertEqual(self.account.client_number, 1010)

    def test_balance_property(self):
        self.assertEqual(round(self.account.balance, 2), 6764.67)

    def test_update_balance_with_valid_amount(self):
        self.account.update_balance(100.0)
        self.assertEqual(
            round(self.account._BankAccount__balance, 2), 6864.67
        )

    def test_update_balance_with_invalid_amount_does_not_change_balance(self):
        self.account.update_balance("invalid")
        self.assertEqual(
            round(self.account._BankAccount__balance, 2), 6764.67
        )

    def test_deposit_valid_amount(self):
        self.account.deposit(200.0)
        self.assertEqual(
            round(self.account._BankAccount__balance, 2), 6964.67
        )

    def test_deposit_non_numeric_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit("abc")
        self.assertIn("must be numeric", str(context.exception))

    def test_deposit_negative_amount_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100.0)
        self.assertIn("must be positive", str(context.exception))

    def test_withdraw_valid_amount(self):
        self.account.withdraw(500.0)
        self.assertEqual(
            round(self.account._BankAccount__balance, 2), 6264.67
        )

    def test_withdraw_non_numeric_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw("xyz")
        self.assertIn("must be numeric", str(context.exception))

    def test_withdraw_negative_amount_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-50.0)
        self.assertIn("must be positive", str(context.exception))

    def test_withdraw_exceeding_balance_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(10000.0)
        self.assertIn(
            "must not exceed the account balance", str(context.exception)
        )

    def test_str_method_format(self):
        expected = "Account Number: 20019 Balance: $6,764.67\n"
        self.assertEqual(str(self.account), expected)


if __name__ == "__main__":
    unittest.main()