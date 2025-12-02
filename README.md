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

# Assignment 4: GUI Development with PySide6 and Event-Driven Programming

- Event-Driven Programming Paradigm
  This application employs the Event-Driven Programming Paradigm through PySide6 to create a responsive graphical user interface for the PiXELL-River Financial banking system. The paradigm is implemented as follows:
## Event Sources and Handlers
- The application responds to user interactions through various event handlers:

- Button Click Events: The lookup_button, deposit_button, withdraw_button, and exit_button all emit clicked signals that are connected to specific handler methods (slots) to process user actions.
- Text Input Events: The client_number_edit widget emits a textChanged signal whenever the user modifies the input, triggering the clearing of the account table to maintain UI consistency.
- Table Selection Events: The account_table widget emits a cellClicked signal when a user selects an account, which opens the account details dialog for transaction processing.

## Signal-Slot Mechanism
- The application uses PySide6's signal-slot mechanism to establish connections between events and their handlers:

- Predefined Signals: Built-in Qt signals like clicked, textChanged, and cellClicked are connected to custom slot methods that implement the business logic.
- Custom Signals: A custom balance_updated signal is defined in AccountDetailsWindow to notify the ClientLookupWindow when a transaction is completed, demonstrating inter-window communication.

## Data Flow and Updates
- The event-driven architecture ensures seamless data flow:

  User actions trigger events (button clicks, text changes, cell selections)
  Event handlers (slots) process the events and update the application state
  The UI is refreshed to reflect the updated state
  Custom signals propagate changes across different windows
  Data persistence is maintained by updating the CSV files through the update_data function

## Benefits of Event-Driven Design

- Responsiveness: The application remains responsive to user input, processing events as they occur without blocking the UI
Modularity: Each event handler is a separate method with a single responsibility, making the code easier to maintain and test

- Loose Coupling: The signal-slot mechanism decouples event sources from event handlers, allowing flexible connections between components
State Management: Events trigger state changes in a controlled manner, ensuring data consistency across the application

This event-driven approach creates an interactive banking application where all functionality is triggered by user actions, providing an intuitive and responsive user experience.

# Assugnment 5 : Filtering Algorithm, Documentation Generation, and Application Distribution

Got it 👍 — you want the documentation rewritten in a **clean, assignment-style format** (like your Event-Driven Programming example). Here’s your **Filtering + Documentation + Distribution** section reformatted to match that style:

---

# Assignment 4: GUI Development with PySide6 and Event-Driven Programming  

## Filtering  
The application integrates a custom filtering algorithm in the **ClientLookupWindow** to allow users to dynamically filter account data.  

### Filter Algorithm Implementation  
- **Input:**  
  - Rows in the `account_table` widget  
  - Filter criteria = selected column (Account Number, Balance, Date Created, Account Type) + search text  

- **Process:**  
  ```python
  for i in range(self.account_table.rowCount()):
  ```
  - Retrieve item at row/column  
  - Compare item text with search text (case-insensitive)  
  - Use `setRowHidden()` to hide non-matching rows  

- **Output:**  
  - Only matching rows remain visible  
  - Non-matching rows are hidden but preserved  
  - Reset restores the full dataset  

### User Interface Integration  
- **Filter Toggle:** Button switches between "Apply Filter" and "Reset"  
- **Dynamic Controls:** Combo box and text field disabled while filtering is active  
- **Status Label:** Displays whether data is filtered  
- **Reset:** Restores all rows and re-enables controls  

### Benefits  
- Demonstrates iteration and conditional logic  
- Efficient for dataset size  
- Flexible for new criteria  
- Self-contained, no external dependencies  

## HTML Documentation  
Sphinx was used to generate professional HTML documentation:  
- Class and method descriptions  
- Parameter and return type details  
- Complete docstrings  
- Cross-references between modules  
- Accessible via `build/html/index.html`  

## Application Distribution  
The application was packaged for distribution using **PyInstaller** and **Inno Setup**.  

### Executable Creation  
- PyInstaller bundles code, libraries, and CSV data  
- Runs without Python installed  
- Dependencies resolved automatically  

### Installer Development  
- Custom branding with name, version, publisher  
- EULA and system requirements displayed  
- Desktop shortcut and uninstaller included  
- Professional wizard with progress indicators  

### Distribution Benefits  
- Easy installation for end users  
- Polished, professional appearance  
- Proper Windows integration  
- Reliable execution across systems  
- Embedded version info for updates  