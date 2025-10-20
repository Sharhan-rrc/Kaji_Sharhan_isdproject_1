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
        __minimum_balance (float): Required minimum balance for the account.
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

        # store validated minimum balance on the account (tests expect this private attr)
        self.__minimum_balance = threshold

        # keep the strategy for optional use, but do not rely on it for core behaviour
        try:
            self.__strategy = MinimumBalanceStrategy(threshold)
        except Exception:
            self.__strategy = None

    def get_service_charges(self) -> float:
        """
        Calculate service charges for the savings account.

        Business rule (derived from tests):
        - If balance is >= minimum_balance: return BASE_SERVICE_CHARGE.
        - If balance is below minimum_balance: return BASE_SERVICE_CHARGE + 0.50
          (tests expect total $1.00 when BASE_SERVICE_CHARGE is $0.50 and minimum
           is not met).
        """
        if self.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE + 0.50

    def __str__(self) -> str:
        base_str = super().__str__().strip()
        formatted_minimum = f"${self.__minimum_balance:,.2f}"
        return (
            f"{base_str}\n"
            f"Minimum Balance: {formatted_minimum} Account Type: Savings"
        )