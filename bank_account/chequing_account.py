"""
Module: chequing_account
Description: This module defines the ChequingAccount class, a subclass of
BankAccount that represents a chequing account with additional attributes
for overdraft limit and overdraft rate. It includes methods for calculating
service charges based on overdraft status and overrides the string
representation to display chequing-specific details.
"""

from bank_account.bank_account import BankAccount
from datetime import date


class ChequingAccount(BankAccount):
    """
    Represents a chequing account, which extends BankAccount with overdraft capabilities.

    Attributes:
        __overdraft_limit (float): The maximum negative balance allowed before overdraft fees apply.
        __overdraft_rate (float): The rate used to calculate overdraft fees when the balance exceeds the limit.
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
        Initializes a ChequingAccount instance.

        Args:
            account_number (int): Unique account number.
            client_number (int): Unique client number.
            balance (float): Initial account balance.
            date_created (date): Date the account was created.
            overdraft_limit (float): Maximum allowable negative balance before fees apply.
            overdraft_rate (float): Rate used to calculate overdraft fees.

        Notes:
            - If overdraft_limit is not convertible to float, defaults to -100.0.
            - If overdraft_rate is not convertible to float, defaults to 0.05.
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05

    def get_service_charges(self) -> float:
        """
        Calculates and returns the service charges for the account.

        Returns:
            float: The calculated service charge based on overdraft status.

        Formula:
            If balance >= overdraft_limit:
                service_charge = BASE_SERVICE_CHARGE
            Else:
                service_charge = BASE_SERVICE_CHARGE + (overdraft_limit - balance) * overdraft_rate
        """
        if self.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE

        overdraft_fee = (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        return self.BASE_SERVICE_CHARGE + overdraft_fee

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the ChequingAccount.

        Format:
            Account Number: {value} Balance: ${value}
            Overdraft Limit: ${value} Overdraft Rate: {value}% Account Type: Chequing

        Returns:
            str: A string containing account details and overdraft settings.
        """
        base_str = super().__str__().strip()
        formatted_limit = f"${self.__overdraft_limit:,.2f}"
        formatted_rate = f"{self.__overdraft_rate * 100:.2f}%"

        return (
            f"{base_str}\n"
            f"Overdraft Limit: {formatted_limit} "
            f"Overdraft Rate: {formatted_rate} Account Type: Chequing"
        )