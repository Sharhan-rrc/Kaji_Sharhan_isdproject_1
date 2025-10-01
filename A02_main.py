"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sharhan Kaji"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date, timedelta

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing = ChequingAccount(10001, 1010, -300.00, date.today(), -200.00, 0.05)
except Exception as e:
    print(f"Error creating ChequingAccount: {e}")

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    print(chequing)
    print("Service Charges:", round(chequing.get_service_charges(), 2))
except Exception as e:
    print(f"Error accessing ChequingAccount: {e}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    chequing.deposit(200.00)
    print(chequing)
    print("Service Charges:", round(chequing.get_service_charges(), 2))
except Exception as e:
    print(f"Error updating ChequingAccount: {e}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savings = SavingsAccount(20002, 1010, 1000.00, date.today(), 50.00)
except Exception as e:
    print(f"Error creating SavingsAccount: {e}")

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    print(savings)
    print("Service Charges:", round(savings.get_service_charges(), 2))
except Exception as e:
    print(f"Error accessing SavingsAccount: {e}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    savings.withdraw(960.00)
    print(savings)
    print("Service Charges:", round(savings.get_service_charges(), 2))
except Exception as e:
    print(f"Error updating SavingsAccount: {e}")

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    recent_investment = InvestmentAccount(30003, 1010, 15000.00, date(2020, 1, 1), 2.00)
except Exception as e:
    print(f"Error creating recent InvestmentAccount: {e}")

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
try:
    print(recent_investment)
    print("Service Charges:", round(recent_investment.get_service_charges(), 2))
except Exception as e:
    print(f"Error accessing recent InvestmentAccount: {e}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    old_date = date.today() - timedelta(days=11 * 365.25)
    old_investment = InvestmentAccount(30004, 1010, 20000.00, old_date, 2.00)
except Exception as e:
    print(f"Error creating old InvestmentAccount: {e}")

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
try:
    print(old_investment)
    print("Service Charges:", round(old_investment.get_service_charges(), 2))
except Exception as e:
    print(f"Error accessing old InvestmentAccount: {e}")

print("===================================================")
# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing.withdraw(chequing.get_service_charges())
    savings.withdraw(savings.get_service_charges())
    recent_investment.withdraw(recent_investment.get_service_charges())
    old_investment.withdraw(old_investment.get_service_charges())
except Exception as e:
    print(f"Error applying service charges: {e}")

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
try:
    print(chequing)
    print(savings)
    print(recent_investment)
    print(old_investment)
except Exception as e:
    print(f"Error printing final account states: {e}")