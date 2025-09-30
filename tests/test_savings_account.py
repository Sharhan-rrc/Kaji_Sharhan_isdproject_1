"""
Description: Unit tests for the SavingsAccount class.
Author: Sharhan Kaji
Usage: To execute all tests in the terminal, run:
    python -m unittest tests/test_savings_account.py
"""

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount


class TestSavingsAccount(unittest.TestCase):
    """
    Unit tests for the SavingsAccount class.
    """

    def test_valid_initialization(self):
        """
        Test that valid inputs correctly initialize all attributes.
        """
        account = SavingsAccount(9483914, 1010, 1559.49, date(2025, 9, 30), 50.00)
        self.assertEqual(account.account_number, 9483914)
        self.assertEqual(account.client_number, 1010)
        self.assertEqual(round(account.balance, 2), 1559.49)
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.00)

    def test_invalid_minimum_balance(self):
        """
        Test that an invalid minimum_balance defaults to 50.0.
        """
        account = SavingsAccount(9483914, 1010, 1559.49, date.today(), "invalid")
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.0)

    def test_service_charge_above_minimum(self):
        """
        Test service charge when balance is above minimum_balance.
        """
        account = SavingsAccount(9483914, 1010, 500.00, date.today(), 50.00)
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_service_charge_equal_minimum(self):
        """
        Test service charge when balance equals minimum_balance.
        """
        account = SavingsAccount(9483914, 1010, 50.00, date.today(), 50.00)
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_service_charge_below_minimum(self):
        """
        Test service charge when balance is below minimum_balance.
        """
        account = SavingsAccount(9483914, 1010, 49.99, date.today(), 50.00)
        self.assertEqual(round(account.get_service_charges(), 2), 1.00)

    def test_str_method_format(self):
        """
        Test __str__ output formatting.
        """
        account = SavingsAccount(9483914, 1010, 1559.49, date(2025, 9, 30), 50.00)
        expected = (
            "Account Number: 9483914 Balance: $1,559.49\n"
            "Minimum Balance: $50.00 Account Type: Savings"
        )
        self.assertEqual(str(account), expected)


if __name__ == "__main__":
    unittest.main()