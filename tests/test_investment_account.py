"""
Description: Unit tests for the InvestmentAccount class.
Author: Sharhan Kaji
Usage: To execute all tests in the terminal, run:
    python -m unittest tests/test_investment_account.py
"""

import unittest
from datetime import date, timedelta
from bank_account import *


class TestInvestmentAccount(unittest.TestCase):
    """
    Unit tests for the InvestmentAccount class using shared setup.
    """

    def setUp(self):
        """
        Initializes common test data for InvestmentAccount tests.
        """
        self.valid_account = InvestmentAccount(20019, 1010, 10000.0, date(2024, 1, 1), 1.99)
        self.invalid_fee_account = InvestmentAccount(20019, 1010, 10000.0, date.today(), "invalid")
        self.old_date = date.today() - timedelta(days=11 * 365.25)
        self.ten_years_ago = date.today() - timedelta(days=10 * 365.25)
        self.recent_date = date(2024, 1, 1)

        self.account_old = InvestmentAccount(20019, 1010, 10000.0, self.old_date, 2.00)
        self.account_ten_years = InvestmentAccount(20019, 1010, 10000.0, self.ten_years_ago, 2.00)
        self.account_recent = InvestmentAccount(20019, 1010, 10000.0, self.recent_date, 2.00)

        self.str_waived_account = InvestmentAccount(2341234, 1010, 19329.21, self.old_date, 1.99)
        self.str_fee_account = InvestmentAccount(1948371, 1010, 11329.65, self.recent_date, 2.00)

    def test_valid_initialization(self):
        """
        Test that valid inputs correctly initialize all attributes.
        """
        account = self.valid_account
        self.assertEqual(account.account_number, 20019)
        self.assertEqual(account.client_number, 1010)
        self.assertEqual(round(account.balance, 2), 10000.00)
        self.assertEqual(account._InvestmentAccount__management_fee, 1.99)

    def test_invalid_management_fee(self):
        """
        Test that an invalid management_fee defaults to 2.55.
        """
        account = self.invalid_fee_account
        self.assertEqual(account._InvestmentAccount__management_fee, 2.55)

    def test_service_charge_more_than_10_years_old(self):
        """
        Test service charge when account is older than 10 years.
        """
        account = self.account_old
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_service_charge_exactly_10_years_old(self):
        """
        Test service charge when account is exactly 10 years old.
        """
        account = self.account_ten_years
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_service_charge_within_10_years(self):
        """
        Test service charge when account is newer than 10 years.
        """
        account = self.account_recent
        self.assertEqual(round(account.get_service_charges(), 2), 2.50)

    def test_str_waived_fee(self):
        """
        Test __str__ output when management fee is waived.
        """
        account = self.str_waived_account
        expected = (
            f"Account Number: 2341234 Balance: $19,329.21\n"
            f"Date Created: {self.old_date.isoformat()} Management Fee: Waived Account Type: Investment"
        )
        self.assertEqual(str(account), expected)

    def test_str_with_fee(self):
        """
        Test __str__ output when management fee is applied.
        """
        account = self.str_fee_account
        expected = (
            "Account Number: 1948371 Balance: $11,329.65\n"
            "Date Created: 2024-01-01 Management Fee: $2.00 Account Type: Investment"
        )
        self.assertEqual(str(account), expected)


if __name__ == "__main__":
    unittest.main()