"""
Module: bank_account
Description: This module defines the BankAccount class, which represents
a bank account with attributes for account number, client number, and
balance. It includes methods for depositing, withdrawing, and updating
the account balance.
"""

class BankAccount:
    """
    Represents a bank account with account number, client number, and balance.

    Attributes:
        __account_number (int): The unique account number.
        __client_number (int): The unique client number associated with the account.
        __balance (float): The current balance of the account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float):
        """
        Initializes a BankAccount instance.

        Args:
            account_number (int): The account number.
            client_number (int): The client number.
            balance (float): The initial balance.

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

    @property
    def account_number(self) -> int:
        """
        Returns the account number.

        Returns:
            int: The account number.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Returns the client number.

        Returns:
            int: The client number.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Returns the current balance.

        Returns:
            float: The current balance.
        """
        return self.__balance

    def update_balance(self, amount: float) -> None:
        """
        Updates the account balance by adding the specified amount.

        Args:
            amount (float): The amount to add to the balance.

        Note:
            If the amount is invalid (non-numeric), the balance remains unchanged.
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
            ValueError: If the amount is non-numeric or not positive.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            formatted = f"${amount:,.2f}"
            raise ValueError(
                f"Deposit amount: {formatted} must be positive."
            )
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """
        Withdraws the specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is non-numeric, not positive, or exceeds
                        the current balance.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            formatted = f"${amount:,.2f}"
            raise ValueError(
                f"Withdraw amount: {formatted} must be positive."
            )
        if amount > self.__balance:
            formatted_amount = f"${amount:,.2f}"
            formatted_balance = f"${self.__balance:,.2f}"
            raise ValueError(
                f"Withdraw amount: {formatted_amount} must not exceed the "
                f"account balance: {formatted_balance}."
            )
        self.update_balance(-amount)

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