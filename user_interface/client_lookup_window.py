"""
Module: client_lookup_window
Description: Implements the client lookup window with event handling for viewing client and account information.

This module provides:
- Client lookup functionality by client number
- Display of client information and associated bank accounts
- Navigation to account details for transaction processing
- Event-driven programming implementation with PySide6

"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sharhan Kaji"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
from bank_account.bank_account import BankAccount


class ClientLookupWindow(LookupWindow):
    """
    A window for looking up client information and managing their bank accounts.

    This class extends LookupWindow to provide functionality for:
    - Looking up clients by client number
    - Displaying client details and their associated accounts
    - Opening account details for transactions
    - Updating account information after transactions

    Attributes:
        client_listing (dict): Dictionary of client_number to Client objects
        accounts (dict): Dictionary of account_number to BankAccount objects
    """

    def __init__(self):
        """
        Initializes the ClientLookupWindow by loading data and connecting events.
        """
        super().__init__()

        self.client_listing, self.accounts = load_data()

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)

    def __on_lookup_client(self) -> None:
        """
        Handles the lookup button click event to display client and account information.

        Retrieves the client by client number and displays their information along with
        all associated bank accounts. Shows error messages if the client number is invalid
        or not found.
        """
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.critical(
                self,
                "Invalid Client Number",
                "Client Number must be an integer value."
            )
            self.reset_display()
            return

        if client_number not in self.client_listing:
            QMessageBox.critical(
                self,
                "Client Not Found",
                f"No client found with Client Number: {client_number}"
            )
            self.reset_display()
            return

        client = self.client_listing[client_number]
        client_name = f"{client.first_name} {client.last_name}"
        self.client_info_label.setText(client_name)

        self.account_table.setRowCount(0)

        row = 0
        for account in self.accounts.values():
            if account.client_number == client.client_number:
                self.account_table.insertRow(row)

                account_number_item = QTableWidgetItem(str(account.account_number))
                account_number_item.setTextAlignment(Qt.AlignCenter)

                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                date_created_item = QTableWidgetItem(str(account._date_created))
                date_created_item.setTextAlignment(Qt.AlignCenter)

                account_type_item = QTableWidgetItem(account.__class__.__name__)
                account_type_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                self.account_table.setItem(row, 0, account_number_item)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, date_created_item)
                self.account_table.setItem(row, 3, account_type_item)

                row += 1

        self.account_table.resizeColumnsToContents()

    def __on_text_changed(self) -> None:
        """
        Handles the text changed event for the client number input field.

        Clears the account table when the user modifies the client number input.
        """
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        """
        Handles the cell clicked event for the account table.

        Opens the account details window for the selected account to allow
        transaction processing.

        Args:
            row (int): The row index of the clicked cell
            column (int): The column index of the clicked cell
        """
        account_number_item = self.account_table.item(row, 0)

        if account_number_item is None:
            QMessageBox.critical(
                self,
                "Selection Error",
                "No account selected. Please select a valid account."
            )
            return

        account_number_text = account_number_item.text()

        if not account_number_text:
            QMessageBox.critical(
                self,
                "Selection Error",
                "No account selected. Please select a valid account."
            )
            return

        try:
            account_number = int(account_number_text)
        except ValueError:
            QMessageBox.critical(
                self,
                "Selection Error",
                "Invalid account number selected."
            )
            return

        if account_number not in self.accounts:
            QMessageBox.critical(
                self,
                "Account Not Found",
                f"No account found with Account Number: {account_number}"
            )
            return

        account = self.accounts[account_number]
        details_window = AccountDetailsWindow(account)

        details_window.balance_updated.connect(self.__update_data)

        details_window.exec_()

    @Slot(BankAccount)
    def __update_data(self, account: BankAccount) -> None:
        """
        Updates the account data after a transaction has been processed.

        Updates the balance display in the account table, updates the accounts
        dictionary, and writes the changes to the CSV file.

        Args:
            account (BankAccount): The updated bank account object
        """
        for row in range(self.account_table.rowCount()):
            account_number_item = self.account_table.item(row, 0)
            if account_number_item and int(account_number_item.text()) == account.account_number:
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.account_table.setItem(row, 1, balance_item)
                break

        self.accounts[account.account_number] = account

        update_data(account)