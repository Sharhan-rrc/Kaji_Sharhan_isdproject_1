"""
Module: bank_account
Description: Defines the BankAccount class with core account functionality and observer support.
"""

from datetime import date
from abc import ABC
from patterns.observer.subject import Subject


class BankAccount(Subject, ABC):
    """
    Represents a bank account with observer notification capabilities.

    Attributes:
        __account_number (int): Unique account number.
        __client_number (int): Unique client number.
        __balance (float): Current account balance.
        _date_created (date): Date the account was created.
    """

    BASE_SERVICE_CHARGE: float = 0.50
    LARGE_TRANSACTION_THRESHOLD: float = 9999.99
    LOW_BALANCE_LEVEL: float = 50.0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        super().__init__()  # Initialize Subject
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0

        self._date_created = date_created if isinstance(date_created, date) else date.today()

    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def client_number(self) -> int:
        return self.__client_number

    @property
    def balance(self) -> float:
        return self.__balance

    def update_balance(self, amount: float) -> None:
        try:
            self.__balance += float(amount)
        except (ValueError, TypeError):
            return

        # Notify if balance is low
        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.__balance:,.2f}: on account {self.__account_number}.")

        # Notify if transaction is large
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${abs(amount):,.2f}: on account {self.__account_number}.")

    def deposit(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} must be positive.")
        if amount > self.__balance:
            raise ValueError(
                f"Withdraw amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}."
            )
        self.update_balance(-amount)

    def get_service_charges(self) -> float:
        return self.BASE_SERVICE_CHARGE

    def __str__(self) -> str:
        formatted_balance = f"${self.__balance:,.2f}"
        return f"Account Number: {self.__account_number} Balance: {formatted_balance}\n"