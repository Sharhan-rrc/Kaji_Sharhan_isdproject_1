"""
Module: savings_account
Description: This module defines the SavingsAccount class, a subclass of
BankAccount that represents a savings account with a minimum balance
requirement. It includes methods for calculating service charges based on
whether the account balance meets or falls below the minimum threshold,
and overrides the string representation to display savings-specific details.
"""

from bank_account.bank_account import BankAccount
from datetime import date


class SavingsAccount(BankAccount):
    """
    Represents a savings account, extending BankAccount with minimum balance logic.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float): Multiplier applied to base service charge if balance is below minimum.
        __minimum_balance (float): Minimum required balance before premium charges apply.
    """

    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        minimum_balance: float
    ):
        """
        Initializes a SavingsAccount instance.

        Args:
            account_number (int): Unique account number.
            client_number (int): Unique client number.
            balance (float): Initial account balance.
            date_created (date): Date the account was created.
            minimum_balance (float): Minimum required balance.

        Notes:
            - If minimum_balance is not convertible to float, defaults to 50.0.
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50.0

    def get_service_charges(self) -> float:
        """
        Calculates and returns the service charges for the account.

        Returns:
            float: BASE_SERVICE_CHARGE if balance >= minimum_balance,
                   otherwise BASE_SERVICE_CHARGE * SERVICE_CHARGE_PREMIUM.
        """
        if self.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the SavingsAccount.

        Format:
            Account Number: {value} Balance: ${value}
            Minimum Balance: ${value} Account Type: Savings

        Returns:
            str: A string containing account details and minimum balance.
        """
        base_str = super().__str__().strip()
        formatted_minimum = f"${self.__minimum_balance:,.2f}"

        return (
            f"{base_str}\n"
            f"Minimum Balance: {formatted_minimum} Account Type: Savings"
        )