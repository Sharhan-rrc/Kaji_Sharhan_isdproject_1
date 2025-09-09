class BankAccount:
    def __init__(self, account_number: int, client_number: int, balance: float):
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
        return self.__account_number

    @property
    def client_number(self) -> int:
        return self.__client_number

    @property
    def balance(self) -> float:
        return self.__balance

    def update_balance(self, amount: float) -> None:
        try:
            amount = float(amount)
            self.__balance += amount
        except (ValueError, TypeError):
            pass  # Do not update balance if amount is invalid

    def deposit(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            formatted = f"${amount:,.2f}"
            raise ValueError(
                f"Deposit amount: {formatted} must be positive."
            )
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
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
        formatted_balance = f"${self.__balance:,.2f}"
        return (
            f"Account Number: {self.__account_number} "
            f"Balance: {formatted_balance}\n"
        )