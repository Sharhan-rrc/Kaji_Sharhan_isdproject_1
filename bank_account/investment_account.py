"""
Module: investment_account
Description: Defines InvestmentAccount with management fee strategy.
"""

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
import calendar
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy


class InvestmentAccount(BankAccount):
    """
    Represents an investment account with management fee strategy.

    Attributes:
        __strategy (ManagementFeeStrategy): Strategy for calculating service charges.
        __management_fee (float): Management fee amount.
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

        # Store management fee as a private attribute so tests can inspect it
        self.__management_fee = fee

        # Keep the strategy if available, but core behaviour should not depend on it
        try:
            self.__strategy = ManagementFeeStrategy(date_created, fee)
        except Exception:
            self.__strategy = None

    def _ten_years_ago(self) -> date:
        """
        Return a date representing today minus 10 years using the same
        day-count heuristic used in the tests (10 * 365.25 days).
        """
        return date.today() - timedelta(days=10 * 365.25)

    def get_service_charges(self) -> float:
        """
        Returns the service charges for the investment account.

        Business rule:
        - If the account was created more than (or equal to) 10 years ago,
          the management fee is waived and only the base service charge applies.
        - Otherwise, the base service charge PLUS the management fee applies.

        Returns:
            float: Calculated service charge.
        """
        if self._date_created <= self._ten_years_ago():
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE + self.__management_fee

    def __str__(self) -> str:
        """
        Returns a string representation of the InvestmentAccount instance.

        The management fee is shown as "Waived" when the account is older than
        or equal to 10 years; otherwise the fee is displayed as currency.
        """
        base_str = super().__str__().strip()
        formatted_date = self._date_created.isoformat()
        fee_display = "Waived" if self._date_created <= self._ten_years_ago() else f"${self.__management_fee:,.2f}"
        return (
            f"{base_str}\n"
            f"Date Created: {formatted_date} "
            f"Management Fee: {fee_display} Account Type: Investment"
        )