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
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy


class InvestmentAccount(BankAccount):
    """
    Represents an investment account with management fee strategy.
    Extends BankAccount to add management fee functionality based on account age.

    Attributes:
        _InvestmentAccount__strategy (ManagementFeeStrategy): Strategy for calculating service charges
        _InvestmentAccount__management_fee (float): Management fee amount
        _date_created (date): Date the account was created

    Business Rules:
        - Default management fee is 2.55 if invalid input provided
        - Management fee is waived for accounts 10 years or older
        - Service charges include base charge plus management fee for accounts under 10 years

    Raises:
        ValueError: If account_number is not an integer (from parent class)
        ValueError: If client_number is not an integer (from parent class)
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
            ValueError: If account_number is not an integer (from parent class)
            ValueError: If client_number is not an integer (from parent class)
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
            Uses 365.25 days per year to account for leap years
        """
        result = date.today() - timedelta(days=10 * 365.25)
        return result

    def get_service_charges(self) -> float:
        """
        Calculate service charges using the management fee strategy.

        Returns:
            float: Total service charges calculated by the strategy

        Note:
            Delegates to ManagementFeeStrategy for charge calculation based on
            account age and management fee. Falls back to manual calculation if strategy fails.
        """
        result = self.BASE_SERVICE_CHARGE

        if self.__strategy is not None:
            result = self.__strategy.calculate_charges(self._date_created)
        elif self._date_created > self._ten_years_ago():
            result = self.BASE_SERVICE_CHARGE + self.__management_fee

        return result

    def __str__(self) -> str:
        """
        Create a detailed string representation of the investment account.

        Returns:
            str: Formatted string containing account number, balance,
                 creation date, management fee status, and account type
        """
        base_string = super().__str__().strip()
        formatted_date = self._date_created.isoformat()

        if self._date_created <= self._ten_years_ago():
            fee_display = "Waived"
        else:
            fee_display = f"${self.__management_fee:,.2f}"

        result = (
            f"{base_string}\n"
            f"Date Created: {formatted_date} "
            f"Management Fee: {fee_display} Account Type: Investment"
        )
        return result