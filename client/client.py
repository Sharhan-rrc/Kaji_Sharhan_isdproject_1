from email_validator import validate_email, EmailNotValidError

class Client:
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self._client_number = client_number

        # Validate first_name
        stripped_first_name = first_name.strip()
        if not stripped_first_name:
            raise ValueError("First name cannot be blank.")
        self._first_name = stripped_first_name

        # Validate last_name
        stripped_last_name = last_name.strip()
        if not stripped_last_name:
            raise ValueError("Last name cannot be blank.")
        self._last_name = stripped_last_name

        # Validate email_address
        try:
            validate_email(email_address)
            self._email_address = email_address
        except EmailNotValidError:
            self._email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        return self._client_number

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def email_address(self) -> str:
        return self._email_address

    def __str__(self) -> str:
        return f"{self._last_name}, {self._first_name} [{self._client_number}] - {self._email_address}\n"