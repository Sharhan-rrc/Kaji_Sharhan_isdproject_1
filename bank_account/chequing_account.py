"""
Module: chequing_account
Description: Defines ChequingAccount with overdraft strategy.

This module provides:
- Chequing account implementation with overdraft capabilities
- Service charge calculations based on overdraft status
- Integration with overdraft strategy pattern
- Custom string representation for account details

Author: ACE Faculty
Version: 1.0.0
"""

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):
    """
    Represents a chequing account with overdraft capabilities.
    Extends BankAccount to add overdraft limit and rate functionality.

    Attributes:
        _ChequingAccount__overdraft_limit (float): Maximum allowed overdraft amount, typically negative
        _ChequingAccount__overdraft_rate (float): Interest rate applied to overdrawn amounts
        _ChequingAccount__strategy (OverdraftStrategy): Strategy for calculating overdraft charges

    Business Rules:
        - Default overdraft limit is -100.0 if invalid input provided
        - Default overdraft rate is 0.05 (5%) if invalid input provided
        - Service charges increase when balance falls below overdraft limit

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
        overdraft_limit: float,
        overdraft_rate: float
    ):
        """
        Initialize a chequing account with overdraft capabilities.

        Args:
            account_number (int): Unique identifier for the account
            client_number (int): Associated client's identifier
            balance (float): Initial monetary balance
            date_created (date): Account creation date
            overdraft_limit (float): Maximum allowed overdraft (typically negative)
            overdraft_rate (float): Interest rate for overdraft calculations

        Raises:
            ValueError: If account_number is not an integer (from parent class)
            ValueError: If client_number is not an integer (from parent class)
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            limit = float(overdraft_limit)
        except (ValueError, TypeError):
            limit = -100.0

        try:
            rate = float(overdraft_rate)
        except (ValueError, TypeError):
            rate = 0.05

        self.__overdraft_limit = limit
        self.__overdraft_rate = rate

        try:
            self.__strategy = OverdraftStrategy(limit, rate)
        except Exception:
            self.__strategy = None

    def get_service_charges(self) -> float:
        """
        Calculate service charges using the overdraft strategy.

        Returns:
            float: Total service charges calculated by the strategy

        Note:
            Delegates to OverdraftStrategy for charge calculation based on balance
            and overdraft limit. Falls back to manual calculation if strategy fails.
        """
        result = self.BASE_SERVICE_CHARGE

        if self.__strategy is not None:
            result = self.__strategy.calculate_charges(self.balance)
        elif self.balance < self.__overdraft_limit:
            result = self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance) * self.__overdraft_rate

        return result

    def __str__(self) -> str:
        """
        Create a detailed string representation of the chequing account.

        Returns:
            str: Formatted string containing account number, balance,
                 overdraft limit, rate, and account type
        """
        base_string = super().__str__().strip()
        formatted_limit = f"${self.__overdraft_limit:,.2f}"
        formatted_rate = f"{self.__overdraft_rate * 100:.2f}%"
        result = (
            f"{base_string}\n"
            f"Overdraft Limit: {formatted_limit} "
            f"Overdraft Rate: {formatted_rate} Account Type: Chequing"
        )
        return result