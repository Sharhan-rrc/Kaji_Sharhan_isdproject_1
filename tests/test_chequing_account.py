"""
Description: Unit tests for the ChequingAccount class.
Author: Sharhan Kaji
Usage: To execute all tests in the terminal, run:
    python -m unittest tests/test_chequing_account.py
"""

import unittest
from datetime import date
from bank_account import *


class TestChequingAccount(unittest.TestCase):
    """
    Unit tests for the ChequingAccount class using shared setup.
    """

    def setUp(self):
        """
        Initializes common test data for ChequingAccount tests.
        """
        self.valid_account = ChequingAccount(20019, 1010, 1000.0, date(2025, 9, 30), -200.0, 0.10)
        self.invalid_limit_account = ChequingAccount(20019, 1010, 1000.0, date.today(), "invalid", 0.10)
        self.invalid_rate_account = ChequingAccount(20019, 1010, 1000.0, date.today(), -200.0, "invalid")
        self.invalid_date_account = ChequingAccount(20019, 1010, 1000.0, "invalid", -200.0, 0.10)

        self.above_limit_account = ChequingAccount(20019, 1010, 500.0, date.today(), -100.0, 0.05)
        self.below_limit_account = ChequingAccount(20019, 1010, -600.0, date.today(), -100.0, 0.05)
        self.equal_limit_account = ChequingAccount(20019, 1010, -100.0, date.today(), -100.0, 0.05)

        self.str_format_account = ChequingAccount(1234567, 1010, 1559.49, date.today(), -150.0, 0.05)

    def test_valid_initialization(self):
        """
        Test that valid inputs correctly initialize all attributes.
        """
        account = self.valid_account
        self.assertEqual(account.account_number, 20019)
        self.assertEqual(account.client_number, 1010)
        self.assertEqual(round(account.balance, 2), 1000.00)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -200.0)
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.10)

    def test_invalid_overdraft_limit(self):
        """
        Test that an invalid overdraft_limit defaults to -100.0.
        """
        account = self.invalid_limit_account
        self.assertEqual(account._ChequingAccount__overdraft_limit, -100.0)

    def test_invalid_overdraft_rate(self):
        """
        Test that an invalid overdraft_rate defaults to 0.05.
        """
        account = self.invalid_rate_account
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_invalid_date_created(self):
        """
        Test that an invalid date_created defaults to today's date.
        """
        account = self.invalid_date_account
        self.assertEqual(account._date_created, date.today())

    def test_service_charge_balance_above_limit(self):
        """
        Test service charge when balance is above overdraft limit.
        """
        account = self.above_limit_account
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_service_charge_balance_below_limit(self):
        """
        Test service charge when balance is below overdraft limit.
        """
        account = self.below_limit_account
        self.assertEqual(round(account.get_service_charges(), 2), 25.50)

    def test_service_charge_balance_equal_limit(self):
        """
        Test service charge when balance equals overdraft limit.
        """
        account = self.equal_limit_account
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_str_method_format(self):
        """
        Test the string representation of ChequingAccount.
        """
        account = self.str_format_account
        expected = (
            "Account Number: 1234567 Balance: $1,559.49\n"
            "Overdraft Limit: $-150.00 Overdraft Rate: 5.00% Account Type: Chequing"
        )
        self.assertEqual(str(account), expected)


if __name__ == "__main__":
    unittest.main()