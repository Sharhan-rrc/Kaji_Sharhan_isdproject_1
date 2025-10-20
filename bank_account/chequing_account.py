"""
Module: chequing_account
Description: Defines ChequingAccount with overdraft strategy.
"""

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):
    """
    Represents a chequing account with overdraft strategy.

    Attributes:
        __strategy (OverdraftStrategy): Strategy for calculating overdraft service charges.
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
        super().__init__(account_number, client_number, balance, date_created)

        try:
            limit = float(overdraft_limit)
        except (ValueError, TypeError):
            limit = -100.0

        try:
            rate = float(overdraft_rate)
        except (ValueError, TypeError):
            rate = 0.05

        self.__strategy = OverdraftStrategy(limit, rate, overdraft_fee=0.0)

    def get_service_charges(self) -> float:
        return self.__strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        base_str = super().__str__().strip()
        formatted_limit = f"${self.__strategy._overdraft_limit:,.2f}"
        formatted_rate = f"{self.__strategy._overdraft_rate * 100:.2f}%"
        return (
            f"{base_str}\n"
            f"Overdraft Limit: {formatted_limit} "
            f"Overdraft Rate: {formatted_rate} Account Type: Chequing"
        )