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
    A dialog window for displaying account details and performing bank account transactions.

    This class extends DetailsWindow to provide functionality for:
    - Displaying account number and current balance
    - Processing deposit transactions
    - Processing withdrawal transactions
    - Emitting signals when balance is updated

    Attributes:
        account (BankAccount): A copy of the bank account being processed
        balance_updated (Signal): Signal emitted when account balance is updated

    Signals:
        balance_updated(BankAccount): Emitted after successful transaction with updated account
    """

    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the AccountDetailsWindow.

        Args:
            account (BankAccount): The bank account to be displayed and processed

        Returns:
            None
        """
        super().__init__()

        if isinstance(account, BankAccount):
            self.account = copy.copy(account)

            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            self.reject()

    def __on_apply_transaction(self) -> None:
        """
        Handles deposit and withdraw button click events to process transactions.

        Validates the transaction amount, processes the appropriate transaction
        (deposit or withdrawal), updates the balance display, and emits a signal
        with the updated account. Shows error messages if the transaction fails.
        """
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.critical(
                self,
                "Invalid Amount",
                "Transaction Amount must be numeric."
            )
            self.transaction_amount_edit.setFocus()
            return

        transaction_type = ""

        try:
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)
            elif self.sender() == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)

            self.balance_label.setText(f"${self.account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

            self.balance_updated.emit(self.account)

        except Exception as e:
            QMessageBox.critical(
                self,
                f"{transaction_type} Error",
                f"{transaction_type} Failed: {str(e)}"
            )
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    def __on_exit(self) -> None:
        """
        Handles the exit button click event to close the dialog window.

        Closes the account details window and returns the user to the client lookup window.
        """
        self.close()
