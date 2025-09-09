"""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "Sharhan Kaji"
__version__ = "1.0.0"
__credits__ = ""

from bank_account.bank_account import BankAccount
from client.client import Client


def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # 1. Code a statement which creates a valid instance of the Client 
    # class.
    try:
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")
    except Exception as e:
        print(e)

    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

    # 3. Instantiate the BankAccount object using valid inputs.
    try:
        bank_account = BankAccount(20019, client.client_number, 6764.67)
    except Exception as e:
        print(e)

    # 4. Create a BankAccount instance with an INVALID balance value.
    try:
        invalid_account = BankAccount(
            20020, client.client_number, "invalid-balance"
        )
    except Exception as e:
        print(e)

    # 5. Print the Client and BankAccount instances.
    print(client)
    print(bank_account)

    # 6. Attempt to deposit a non-numeric value.
    try:
        bank_account.deposit("abc")
    except Exception as e:
        print(e)

    # 7. Attempt to deposit a negative value.
    try:
        bank_account.deposit(-100.00)
    except Exception as e:
        print(e)

    # 8. Attempt to withdraw a valid amount.
    try:
        bank_account.withdraw(500.00)
    except Exception as e:
        print(e)

    # 9. Attempt to withdraw a non-numeric value.
    try:
        bank_account.withdraw("xyz")
    except Exception as e:
        print(e)

    # 10. Attempt to withdraw a negative value.
    try:
        bank_account.withdraw(-50.00)
    except Exception as e:
        print(e)

    # 11. Attempt to withdraw more than the current balance.
    try:
        bank_account.withdraw(10000.00)
    except Exception as e:
        print(e)

    # 12. Print the BankAccount instance again.
    print(bank_account)


if __name__ == "__main__":
    main()