"""
Module: bank_account
Description: Defines the BankAccount abstract base class which implements core banking
functionality and the Subject role in the Observer pattern.

This module provides:
- Basic account operations (deposit, withdraw, balance updates)
- Service charge calculations
- Transaction monitoring and notifications
- Observer pattern integration for client notifications

Classes:
    BankAccount: Abstract base class for all bank account types

Author: ACE Faculty
Version: 1.0.0
"""

from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.subject import Subject


class BankAccount(Subject, ABC):
    """
    Abstract base class representing a bank account with observer notification capabilities.
    Implements the Subject interface to notify observers of significant account events.

    Attributes:
        BASE_SERVICE_CHARGE (float): Base service charge applied to all accounts
        LARGE_TRANSACTION_THRESHOLD (float): Amount above which transactions trigger notifications
        LOW_BALANCE_LEVEL (float): Balance threshold for low balance warnings
        __account_number (int): Unique identifier for the account
        __client_number (int): Associated client's identifier
        __balance (float): Current monetary balance
        _date_created (date): Account creation date
        _observers (list): List of attached observers

    Raises:
        ValueError: If account_number or client_number are not integers
    """

    BASE_SERVICE_CHARGE: float = 0.50
    LARGE_TRANSACTION_THRESHOLD: float = 9999.99
    LOW_BALANCE_LEVEL: float = 50.0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        """
        Initialize a new bank account.

        Args:
            account_number (int): Unique identifier for the account
            client_number (int): Associated client's identifier
            balance (float): Initial monetary balance
            date_created (date): Account creation date

        Raises:
            ValueError: If account_number or client_number are not integers
        """
        super().__init__()

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
        """Get the account number."""
        return self.__account_number

    @property
    def client_number(self) -> int:
        """Get the client number."""
        return self.__client_number

    @property
    def balance(self) -> float:
        """Get the current balance."""
        return self.__balance

    def attach(self, observer) -> None:
        """
        Attach an observer to receive account notifications.

        Args:
            observer: Observer object implementing the Observer interface
        """
        super().attach(observer)

    def detach(self, observer) -> None:
        """
        Detach an observer from account notifications.

        Args:
            observer: Observer object to remove from notification list
        """
        super().detach(observer)

    def notify(self, message: str) -> None:
        """
        Notify all attached observers with a message.

        Args:
            message (str): The notification message to send to all observers
        """
        super().notify(message)

    def update_balance(self, amount: float) -> None:
        """
        Update the account balance and notify observers of significant changes.

        Args:
            amount (float): Amount to add to (positive) or subtract from (negative) balance

        Note:
            Notifications are sent for:
            - Low balance (below LOW_BALANCE_LEVEL)
            - Large transactions (above LARGE_TRANSACTION_THRESHOLD)
        """
        try:
            self.__balance += float(amount)
        except (ValueError, TypeError):
            return

        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.__balance:,.2f}: on account {self.__account_number}.")

        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${abs(amount):,.2f}: on account {self.__account_number}.")

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit

        Raises:
            ValueError: If amount is not numeric or is not positive
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw

        Raises:
            ValueError: If amount is not numeric, not positive, or exceeds balance
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} must be positive.")
        if amount > self.__balance:
            raise ValueError(
                f"Withdraw amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}."
            )
        self.update_balance(-amount)

    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Calculate service charges for the account.

        Returns:
            float: The calculated service charge amount

        Note:
            This is an abstract method that must be implemented by subclasses
        """
        pass

    def __str__(self) -> str:
        """
        Create a string representation of the account.

        Returns:
            str: Formatted string with account number and balance
        """
        formatted_balance = f"${self.__balance:,.2f}"
        return f"Account Number: {self.__account_number} Balance: {formatted_balance}\n"