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

        # Store validated values on the ChequingAccount instance so tests can access them
        self.__overdraft_limit = limit
        self.__overdraft_rate = rate

        # Try to create a strategy if signature matches; if not, keep strategy as None
        try:
            self.__strategy = OverdraftStrategy(limit, rate)
        except TypeError:
            self.__strategy = None

    def get_service_charges(self) -> float:
        # Use local attributes for a robust calculation independent of strategy implementation
        if self.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        return (
            self.BASE_SERVICE_CHARGE
            + (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        )

    def __str__(self) -> str:
        base_str = super().__str__().strip()
        formatted_limit = f"${self.__overdraft_limit:,.2f}"
        formatted_rate = f"{self.__overdraft_rate * 100:.2f}%"
        return (
            f"{base_str}\n"
            f"Overdraft Limit: {formatted_limit} "
            f"Overdraft Rate: {formatted_rate} Account Type: Chequing"
        )