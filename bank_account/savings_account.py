"""
Module: savings_account
Description: Defines SavingsAccount with minimum balance strategy.

This module provides:
- Savings account implementation with minimum balance requirements
- Balance-based service charge calculations
- Integration with minimum balance strategy pattern
- Custom string representation for savings accounts

Author: ACE Faculty
Version: 1.0.0
"""

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy


class SavingsAccount(BankAccount):
    """
    Represents a savings account with minimum balance requirements.
    Extends BankAccount to add minimum balance functionality.

    Attributes:
        __strategy (MinimumBalanceStrategy): Strategy for calculating service charges
        __minimum_balance (float): Required minimum balance for the account

    Business Rules:
        - Default minimum balance is 50.0 if invalid input provided
        - Additional service charge applies when balance falls below minimum
        - Service charges include base charge plus penalty for low balance
    """

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        minimum_balance: float
    ):
        """
        Initialize a savings account with minimum balance requirement.

        Args:
            account_number (int): Unique identifier for the account
            client_number (int): Associated client's identifier
            balance (float): Initial monetary balance
            date_created (date): Account creation date
            minimum_balance (float): Required minimum balance threshold

        Raises:
            ValueError: If account_number or client_number are not integers
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            threshold = float(minimum_balance)
        except (ValueError, TypeError):
            threshold = 50.0

        self.__minimum_balance = threshold

        try:
            self.__strategy = MinimumBalanceStrategy(threshold)
        except Exception:
            self.__strategy = None

    def get_service_charges(self) -> float:
        """
        Calculate service charges using the minimum balance strategy.

        Returns:
            float: Total service charges calculated by the strategy

        Note:
            Delegates to MinimumBalanceStrategy for charge calculation based on
            account balance and minimum balance requirement
        """
        if self.__strategy is not None:
            return self.__strategy.calculate_charges(self.balance)
        
        if self.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE + 0.50

    def __str__(self) -> str:
        """
        Create a detailed string representation of the savings account.

        Returns:
            str: Formatted string containing:
                - Account number and balance (from parent class)
                - Minimum balance requirement in currency format
                - Account type identifier
        """
        base_str = super().__str__().strip()
        formatted_minimum = f"${self.__minimum_balance:,.2f}"
        return (
            f"{base_str}\n"
            f"Minimum Balance: {formatted_minimum} Account Type: Savings"
        )