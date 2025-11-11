"""
Module: account_details_window
Description: Implements the account details window for processing bank transactions.

This module provides:
- Display of account details (account number and balance)
- Deposit transaction processing
- Withdrawal transaction processing
- Signal emission for balance updates
- Transaction validation and error handling

"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sharhan Kaji"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
