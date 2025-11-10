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

# Assignment 3: Strategy and Observer Pattern Integration in Bank Account System

## Strategy Pattern
This project uses the Strategy Pattern to handle service charge calculations for different types of bank accounts. Instead of putting the logic directly in each account class, the calculation is delegated to a strategy class.
Each account type (Chequing, Savings, Investment) has its own strategy:
- Chequing uses OverdraftStrategy
- Savings uses MinimumBalanceStrategy
- Investment uses ManagementFeeStrategy
This makes the code easier to maintain and extend. If you ever need to add new rules or account types, you can just create a new strategy class without changing the existing ones.
All original tests and the client program (A02_main.py) still work as expected, confirming the refactor was successful.

## Observer Pattern
This application uses the Observer Pattern to notify clients of important changes in their bank accounts. Each BankAccount acts as a Subject, and each Client acts as an Observer. Clients can subscribe to accounts, and they receive notifications when:
- A transaction exceeds the large transaction threshold.
- The account balance drops below the minimum level.
Notifications are simulated as emails and saved to output/observer_emails.txt. This design keeps the notification logic separate from account operations, making the system more modular and easier to maintain.

# Assignment 4: [Indicate the name and description of the current assignment]
