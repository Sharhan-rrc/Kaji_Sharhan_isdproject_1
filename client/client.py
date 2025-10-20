"""
Module: client
Description: Defines the Client class, which represents a bank client and acts as an Observer.
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
        __client_number (int): Unique client number.
        __first_name (str): First name of the client.
        __last_name (str): Last name of the client.
        __email_address (str): Email address of the client.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
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
        return self.__client_number

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def email_address(self) -> str:
        return self.__email_address

    def __str__(self) -> str:
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}\n"

    def update(self, message: str) -> None:
        """
        Called when the subject notifies this observer.

        Args:
            message (str): The notification message.
        """
        subject = f"ALERT: Unusual Activity: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        body = (
            f"Notification for {self.__client_number}: "
            f"{self.__first_name} {self.__last_name}: {message}"
        )
        simulate_send_email(self.__email_address, subject, body)