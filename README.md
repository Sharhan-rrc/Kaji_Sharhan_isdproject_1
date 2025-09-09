# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. Each 
assignment will build on the work done in the previous assignment(s). 
Ultimately, an entire system will be created to manage bank transactions for 
clients who have one or more bank accounts.

## Author
Sharhan Kaji

## Assignment
Assignment 1: Financial System Foundations: Class Design & Testing

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
