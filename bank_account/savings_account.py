"""
Module: savings_account
Description: Defines SavingsAccount with minimum balance strategy.
"""

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy


class SavingsAccount(BankAccount):
    """
    Represents a savings account with minimum balance strategy.

    Attributes:
        __strategy (MinimumBalanceStrategy): Strategy for calculating service charges.
    """

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        minimum_balance: float
    ):
        super().__init__(account_number, client_number, balance, date_created)

        try:
            threshold = float(minimum_balance)
        except (ValueError, TypeError):
            threshold = 50.0

        self.__strategy = MinimumBalanceStrategy(threshold)

    def get_service_charges(self) -> float:
        return self.__strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        base_str = super().__str__().strip()
        formatted_minimum = f"${self.__strategy._minimum_balance:,.2f}"
        return (
            f"{base_str}\n"
            f"Minimum Balance: {formatted_minimum} Account Type: Savings"
        )