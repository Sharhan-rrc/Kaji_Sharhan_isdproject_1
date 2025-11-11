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
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    pass
        
