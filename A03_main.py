"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sharhan Kaji"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import Client
from datetime import date

# 2. Create a Client object with data of your choice.
client1 = Client(1010, "Sharhan", "Kaji", "sharhan.kaji@example.com")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing1 = ChequingAccount(10001, client1.client_number, 100.00, date.today(), -200.00, 0.05)
savings1 = SavingsAccount(20001, client1.client_number, 1000.00, date.today(), 50.00)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequing1.attach(client1)
savings1.attach(client1)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
client2 = Client(2020, "Amina", "Rivera", "amina.rivera@example.com")
savings2 = SavingsAccount(20002, client2.client_number, 500.00, date.today(), 50.00)
savings2.attach(client2)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

# Transactions for chequing1
try:
    chequing1.deposit(15000.00)  # triggers large transaction alert
except Exception as e:
    print(e)

try:
    chequing1.withdraw(14900.00)  # triggers low balance alert
except Exception as e:
    print(e)

try:
    chequing1.deposit(100.00)  # normal transaction
except Exception as e:
    print(e)

# Transactions for savings1
try:
    savings1.withdraw(960.00)  # triggers low balance alert
except Exception as e:
    print(e)

try:
    savings1.deposit(10000.00)  # triggers large transaction alert
except Exception as e:
    print(e)

try:
    savings1.withdraw(50.00)  # normal transaction
except Exception as e:
    print(e)

# Transactions for savings2
try:
    savings2.deposit(12000.00)  # triggers large transaction alert
except Exception as e:
    print(e)

try:
    savings2.withdraw(11990.00)  # triggers low balance alert
except Exception as e:
    print(e)

try:
    savings2.deposit(100.00)  # normal transaction
except Exception as e:
    print(e)