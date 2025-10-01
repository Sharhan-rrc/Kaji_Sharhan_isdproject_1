"""
Module: investment_account
Description: This module defines the InvestmentAccount class, a subclass of
BankAccount that represents an investment account with a management fee.
It includes methods for calculating service charges based on account age
and fee eligibility, and overrides the string representation to display
investment-specific details including fee status.
"""

from bank_account.bank_account import BankAccount
from datetime import date, timedelta


class InvestmentAccount(BankAccount):
    """
    Represents an investment account, extending BankAccount with long-term savings features.

    Attributes:
        TEN_YEARS_AGO (date): A constant representing the date 10 years prior to today.
        __management_fee (float): Flat-rate fee charged for managing the account.
    """

    TEN_YEARS_AGO: date = date.today() - timedelta(days=10 * 365.25)

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        management_fee: float
    ):
        """
        Initializes an InvestmentAccount instance.

        Args:
            account_number (int): Unique account number.
            client_number (int): Unique client number.
            balance (float): Initial account balance.
            date_created (date): Date the account was created.
            management_fee (float): Flat-rate management fee.

        Notes:
            - If management_fee is not convertible to float, defaults to 2.55.
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55

    def get_service_charges(self) -> float:
        """
        Calculates and returns the service charges for the account.

        Returns:
            float: BASE_SERVICE_CHARGE if account is older than TEN_YEARS_AGO,
                   otherwise BASE_SERVICE_CHARGE + management_fee.
        """
        if self._date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE + self.__management_fee

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the InvestmentAccount.

        Format:
            Account Number: {value} Balance: ${value}
            Date Created: {value} Management Fee: ${value}/Waived Account Type: Investment

        Returns:
            str: A string containing account details and fee status.
        """
        base_str = super().__str__().strip()
        formatted_date = self._date_created.isoformat()

        if self._date_created <= self.TEN_YEARS_AGO:
            fee_display = "Waived"
        else:
            fee_display = f"${self.__management_fee:,.2f}"

        return (
            f"{base_str}\n"
            f"Date Created: {formatted_date} "
            f"Management Fee: {fee_display} Account Type: Investment"
        )