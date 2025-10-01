# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. Each 
assignment will build on the work done in the previous assignment(s). 
Ultimately, an entire system will be created to manage bank transactions for 
clients who have one or more bank accounts.

## Author
Sharhan Kaji

## Assignment
# Assignment 1: Financial System Foundations: Class Design & Testing

## Encapsulation
- Encapsulation in the `BankAccount` class is implemented by restricting 
  direct access to its internal data. The attributes `account_number`, 
  `client_number`, and `balance` are declared as private using double 
  underscores, which prevents them from being accessed or modified directly 
  from outside the class.
- To interact with these attributes safely, the class provides property 
  methods that expose controlled, read-only access.
- All updates to the account’s state—such as deposits and withdrawals—are 
  handled through dedicated methods that include strict validation and 
  exception handling.
- This ensures that the data remains consistent and protected from unintended
  changes, while still allowing necessary interactions through clearly 
  defined interfaces.

# Assignment 2: Implementing distinct service charge calculation methods for
# Chequing, Investment, and Savings accounts.

## Polymorphism
- Polymorphism in this project is achieved by defining a common interface
 in the BankAccount superclass, specifically through the method 
 get_service_charges(), which is implemented differently in each 
 subclass: ChequingAccount, SavingsAccount, and InvestmentAccount.
- Each subclass overrides the get_service_charges() method to provide 
 distinct logic tailored to its specific type of account.
- This allows the client code to interact with any BankAccount instance 
 polymorphically—calling get_service_charges() without needing to know 
 the exact subclass type.
- By leveraging this approach, the system supports dynamic method dispatch 
 at runtime, enabling flexible and extensible handling of service charge
 calculations. This polymorphic design enhances maintainability and 
 scalability by centralizing shared behavior in the superclass, while 
 allowing specialized behavior in the subclasses.
