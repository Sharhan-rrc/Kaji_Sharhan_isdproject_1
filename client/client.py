"""
Module: client
Description: Defines the Client class, which represents a bank client and acts as an Observer.

This module provides:
- Client information management (name, number, email)
- Email validation and notification handling
- Observer pattern implementation for account notifications
- String representation for client details

Author: ACE Faculty
Version: 1.0.0
"""

from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from email_validator import validate_email, EmailNotValidError
from datetime import datetime


class Client(Observer):
    """
    Represents a client with client number, first name, last name, and email.
    Implements the Observer interface to receive notifications.

    Attributes:
        __client_number (int): Unique identifier for the client
        __first_name (str): Client's first name, non-empty string
        __last_name (str): Client's last name, non-empty string
        __email_address (str): Valid email address or default if invalid

    Business Rules:
        - Client number must be an integer
        - First and last names cannot be blank or whitespace
        - Invalid email addresses default to "email@pixell-river.com"
        - Notifications are sent via email with timestamp
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initialize a new client with basic information.

        Args:
            client_number (int): Unique identifier for the client
            first_name (str): Client's first name
            last_name (str): Client's last name
            email_address (str): Client's email address

        Raises:
            ValueError: If client_number is not an integer
            ValueError: If first_name or last_name is blank after stripping
        """
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        first_name = first_name.strip()
        if not first_name:
            raise ValueError("First name cannot be blank.")
        self.__first_name = first_name

        last_name = last_name.strip()
        if not last_name:
            raise ValueError("Last name cannot be blank.")
        self.__last_name = last_name

        try:
            validate_email(email_address)
            self.__email_address = email_address
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """Get the client's unique identifier number."""
        return self.__client_number

    @property
    def first_name(self) -> str:
        """Get the client's first name."""
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Get the client's last name."""
        return self.__last_name

    @property
    def email_address(self) -> str:
        """Get the client's email address."""
        return self.__email_address

    def __str__(self) -> str:
        """
        Create a string representation of the client.

        Returns:
            str: Formatted string with last name, first name, client number, and email
                 Format: "LastName, FirstName [ClientNumber] - email@address"
        """
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}\n"

    def update(self, message: str) -> None:
        """
        Process notification from observed accounts (Observer pattern implementation).

        Args:
            message (str): The notification message from the observed account

        Note:
            Sends an email notification with:
            - Subject: Current timestamp and "Unusual Activity" alert
            - Body: Client details and the notification message
        """
        subject = f"ALERT: Unusual Activity: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        body = (
            f"Notification for {self.__client_number}: "
            f"{self.__first_name} {self.__last_name}: {message}"
        )
        simulate_send_email(self.__email_address, subject, body)