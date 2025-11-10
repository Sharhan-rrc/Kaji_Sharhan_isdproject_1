"""
Description: A client program written to verify implementation 
of the Observer Pattern.

This module demonstrates:
- Creation and management of bank accounts and clients
- Implementation of Observer pattern for transaction notifications
- Exception handling for banking operations
- Transaction processing with various amounts

Author: ACE Faculty
Version: 1.0.0
Credits: Sharhan Kaji
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import Client
from datetime import date

# 2. Create a Client object with data of your choice.
try:
    client_one = Client(1010, "Sharhan", "Kaji", "sharhan.kaji@example.com")
except ValueError as error:
    print(f"Error creating client one: {error}")
    client_one = None

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
try:
    chequing_one = ChequingAccount(10001, client_one.client_number, 100.00, date.today(), -200.00, 0.05)
except (ValueError, AttributeError) as error:
    print(f"Error creating chequing account one: {error}")
    chequing_one = None

try:
    savings_one = SavingsAccount(20001, client_one.client_number, 1000.00, date.today(), 50.00)
except (ValueError, AttributeError) as error:
    print(f"Error creating savings account one: {error}")
    savings_one = None

if chequing_one and savings_one and client_one:
    chequing_one.attach(client_one)
    savings_one.attach(client_one)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
try:
    client_two = Client(2020, "Amina", "Rivera", "amina.rivera@example.com")
except ValueError as error:
    print(f"Error creating client two: {error}")
    client_two = None

try:
    savings_two = SavingsAccount(20002, client_two.client_number, 500.00, date.today(), 50.00)
except (ValueError, AttributeError) as error:
    print(f"Error creating savings account two: {error}")
    savings_two = None

if savings_two and client_two:
    savings_two.attach(client_two)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

try:
    chequing_one.deposit(15000.00)
except Exception as error:
    print(error)

try:
    chequing_one.withdraw(14900.00)
except Exception as error:
    print(error)

try:
    chequing_one.deposit(100.00)
except Exception as error:
    print(error)

try:
    savings_one.withdraw(960.00)
except Exception as error:
    print(error)

try:
    savings_one.deposit(10000.00)
except Exception as error:
    print(error)

try:
    savings_one.withdraw(50.00)
except Exception as error:
    print(error)

try:
    savings_two.deposit(12000.00)
except Exception as error:
    print(error)

try:
    savings_two.withdraw(11990.00)
except Exception as error:
    print(error)

try:
    savings_two.deposit(100.00)
except Exception as error:
    print(error)