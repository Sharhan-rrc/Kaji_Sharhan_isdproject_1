"""
Module: investment_account
Description: Defines InvestmentAccount with management fee strategy.
"""

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy


class InvestmentAccount(BankAccount):
    """
    Represents an investment account with management fee strategy.

    Attributes:
        __strategy (ManagementFeeStrategy): Strategy for calculating service charges.
    """

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        management_fee: float
    ):
        super().__init__(account_number, client_number, balance, date_created)

        try:
            fee = float(management_fee)
        except (ValueError, TypeError):
            fee = 2.55

        self.__strategy = ManagementFeeStrategy(date_created, fee)

    def get_service_charges(self) -> float:
        return self.__strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        base_str = super().__str__().strip()
        formatted_date = self._date_created.isoformat()
        fee_display = "Waived" if self._date_created <= self.__strategy._TEN_YEARS_AGO else f"${self.__strategy._management_fee:,.2f}"
        return (
            f"{base_str}\n"
            f"Date Created: {formatted_date} "
            f"Management Fee: {fee_display} Account Type: Investment"
        )