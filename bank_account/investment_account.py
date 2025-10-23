"""
Module: investment_account
Description: Defines InvestmentAccount with management fee strategy.

This module provides:
- Investment account implementation with management fee logic
- Age-based service charge calculations
- Integration with management fee strategy pattern
- Custom string representation for investment accounts

Author: ACE Faculty
Version: 1.0.0
"""

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
import calendar
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy


class InvestmentAccount(BankAccount):
    """
    Represents an investment account with management fee strategy.
    Extends BankAccount to add management fee functionality based on account age.

    Attributes:
        __strategy (ManagementFeeStrategy): Strategy for calculating service charges
        __management_fee (float): Management fee amount
        _date_created (date): Date the account was created

    Business Rules:
        - Default management fee is 2.55 if invalid input provided
        - Management fee is waived for accounts 10 years or older
        - Service charges include base charge plus management fee for accounts under 10 years
    """

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        management_fee: float
    ):
        """
        Initialize an investment account with management fee capability.

        Args:
            account_number (int): Unique identifier for the account
            client_number (int): Associated client's identifier
            balance (float): Initial monetary balance
            date_created (date): Account creation date
            management_fee (float): Fee charged for managing the account

        Raises:
            ValueError: If account_number or client_number are not integers
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            fee = float(management_fee)
        except (ValueError, TypeError):
            fee = 2.55

        self.__management_fee = fee

        try:
            self.__strategy = ManagementFeeStrategy(date_created, fee)
        except Exception:
            self.__strategy = None

    def _ten_years_ago(self) -> date:
        """
        Calculate the date exactly 10 years ago from today.

        Returns:
            date: Date object representing 10 years ago

        Note:
            Uses 365.25 days per year to account for leap years in the calculation
        """
        return date.today() - timedelta(days=10 * 365.25)

    def get_service_charges(self) -> float:
        """
        Calculate total service charges based on account age.

        Returns:
            float: Total service charges including:
                  - Base service charge for all accounts
                  - Management fee if account is less than 10 years old

        Note:
            Accounts 10 years or older only pay the base service charge
            Newer accounts pay base charge plus management fee
        """
        if self._date_created <= self._ten_years_ago():
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE + self.__management_fee

    def __str__(self) -> str:
        """
        Create a detailed string representation of the investment account.

        Returns:
            str: Formatted string containing:
                - Account number and balance (from parent class)
                - Account creation date
                - Management fee (shown as "Waived" if account ≥ 10 years)
                - Account type identifier
        """
        base_str = super().__str__().strip()
        formatted_date = self._date_created.isoformat()
        fee_display = "Waived" if self._date_created <= self._ten_years_ago() else f"${self.__management_fee:,.2f}"
        return (
            f"{base_str}\n"
            f"Date Created: {formatted_date} "
            f"Management Fee: {fee_display} Account Type: Investment"
        )