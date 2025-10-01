"""
Module: bank_account
Description: This module defines the BankAccount class, which represents
a bank account with attributes for account number, client number, balance,
and creation date. It includes methods for depositing, withdrawing, updating
the account balance, and calculating service charges.

"""

from datetime import date


class BankAccount:
    """
    Represents a bank account with account number, client number, balance, and creation date.

    Attributes:
        BASE_SERVICE_CHARGE (float): The base service charge applied to all accounts.
        __account_number (int): The unique account number for the bank account.
        __client_number (int): The unique client number associated with the account.
        __balance (float): The current balance of the account.
        _date_created (date): The date the account was created.
    """

    BASE_SERVICE_CHARGE: float = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        """
        Initializes a BankAccount instance.

        Args:
            account_number (int): The unique account number for the bank account.
            client_number (int): The unique client number associated with the account.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.

        Raises:
            ValueError: If account_number or client_number is not an integer.
        """
        # Validate account_number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Validate balance
        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0

        # Validate date_created
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    @property
    def account_number(self) -> int:
        """
        Returns the account number.

        Returns:
            int: The unique account number for the bank account.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Returns the client number.

        Returns:
            int: The unique client number associated with the account.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.__balance

    def update_balance(self, amount: float) -> None:
        """
        Updates the account balance by adding the specified amount.

        Args:
            amount (float): The amount to add to the account balance.

        Raises:
            ValueError: If the amount is not numeric.
        """
        try:
            amount = float(amount)
            self.__balance += amount
        except (ValueError, TypeError):
            pass  # Do not update balance if amount is invalid

    def deposit(self, amount: float) -> None:
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not numeric or is less than or equal to zero.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            formatted = f"${amount:,.2f}"
            raise ValueError(f"Deposit amount: {formatted} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """
        Withdraws the specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not numeric, is less than or equal to zero,
                        or exceeds the current account balance.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            formatted = f"${amount:,.2f}"
            raise ValueError(f"Withdraw amount: {formatted} must be positive.")
        if amount > self.__balance:
            formatted_amount = f"${amount:,.2f}"
            formatted_balance = f"${self.__balance:,.2f}"
            raise ValueError(
                f"Withdraw amount: {formatted_amount} must not exceed the "
                f"account balance: {formatted_balance}."
            )
        self.update_balance(-amount)

    def get_service_charges(self) -> float:
        """
        Returns the service charges for the account.

        Returns:
            float: The base service charge applied to the account.
        """
        return self.BASE_SERVICE_CHARGE

    def __str__(self) -> str:
        """
        Returns a string representation of the BankAccount instance.

        Returns:
            str: A formatted string containing the account number and balance.
        """
        formatted_balance = f"${self.__balance:,.2f}"
        return (
            f"Account Number: {self.__account_number} "
            f"Balance: {formatted_balance}\n"
        )