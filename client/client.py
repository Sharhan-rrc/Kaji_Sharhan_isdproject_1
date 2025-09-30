"""
Module: client
Description: This module defines the Client class, which represents a client
with attributes for client number, first name, last name, and email address.
It includes methods for accessing these attributes and validating email
addresses.
"""

from email_validator import validate_email, EmailNotValidError


class Client:
    """
    Represents a client with client number, first name, last name, and email.

    Attributes:
        __client_number (int): The unique client number.
        __first_name (str): The first name of the client.
        __last_name (str): The last name of the client.
        __email_address (str): The email address of the client.
    """

    def __init__(
        self,
        client_number: int,
        first_name: str,
        last_name: str,
        email_address: str
    ):
        """
        Initializes a Client instance.

        Args:
            client_number (int): The client number.
            first_name (str): The first name of the client.
            last_name (str): The last name of the client.
            email_address (str): The email address of the client.

        Raises:
            ValueError: If client_number is not an integer or if first_name
                        or last_name is blank.
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
        """
        Returns the client number.

        Returns:
            int: The client number.
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """
        Returns the first name of the client.

        Returns:
            str: The first name.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Returns the last name of the client.

        Returns:
            str: The last name.
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Returns the email address of the client.

        Returns:
            str: The email address.
        """
        return self.__email_address

    def __str__(self) -> str:
        """
        Returns a string representation of the Client instance.

        Returns:
            str: A formatted string containing the client's details.
        """
        return (
            f"{self.__last_name}, {self.__first_name} "
            f"[{self.__client_number}] - {self.__email_address}\n"
        )