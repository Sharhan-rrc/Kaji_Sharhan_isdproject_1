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
        __overdraft_limit (float): Maximum allowed overdraft amount, typically negative
        __overdraft_rate (float): Interest rate applied to overdrawn amounts
        __strategy (OverdraftStrategy): Optional strategy for calculating overdraft charges

    Business Rules:
        - Default overdraft limit is -100.0 if invalid input provided
        - Default overdraft rate is 0.05 (5%) if invalid input provided
        - Service charges increase when balance falls below overdraft limit
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
            ValueError: If account_number or client_number are not integers
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
        except TypeError:
            self.__strategy = None

    def get_service_charges(self) -> float:
        """
        Calculate service charges based on account balance and overdraft status.

        Returns:
            float: Total service charges including:
                  - Base service charge for all accounts
                  - Additional charges if balance is below overdraft limit

        Note:
            Charges = BASE_SERVICE_CHARGE + overdraft_penalty
            where overdraft_penalty = (overdraft_limit - balance) * overdraft_rate
            if balance is below overdraft_limit
        """
        if self.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        return (
            self.BASE_SERVICE_CHARGE
            + (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        )

    def __str__(self) -> str:
        """
        Create a detailed string representation of the chequing account.

        Returns:
            str: Formatted string containing:
                - Account number and balance (from parent class)
                - Overdraft limit in currency format
                - Overdraft rate as percentage
                - Account type identifier
        """
        base_str = super().__str__().strip()
        formatted_limit = f"${self.__overdraft_limit:,.2f}"
        formatted_rate = f"{self.__overdraft_rate * 100:.2f}%"
        return (
            f"{base_str}\n"
            f"Overdraft Limit: {formatted_limit} "
            f"Overdraft Rate: {formatted_rate} Account Type: Chequing"
        )