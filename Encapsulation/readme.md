# **Encapsulation in Bank Accounts**

This folder contains an example of implementing **Encapsulation**, a core principle of object-oriented programming (OOP), using Python. It models a **banking system** that ensures secure access to user information and provides methods to perform banking operations like checking balances, deposits, withdrawals, and password management.

---

## **Features**
- Encapsulation of user data to ensure secure access and modification.
- Getter and setter methods to manipulate private attributes safely.
- A `BankAccount` class to manage multiple users and their banking operations.
- Comprehensive error handling for invalid operations.

---

## **Classes and Methods**

### **`User` Class**
Represents a user in the banking system.  

**Attributes**:
- `name` (public): Name of the user.
- `__phone` (private): User's phone number.
- `__balance` (private): User's account balance.
- `__password` (private): User's account password.

**Methods**:
- `get_phone()`: Returns the phone number.
- `get_balance()`: Returns the account balance.
- `set_balance(amount)`: Sets the balance (validates non-negative values).
- `verify_password(password)`: Verifies the user's password.
- `set_password(new_password)`: Updates the password.

---

### **`BankAccount` Class**
Manages banking operations for multiple users.  

**Methods**:
- `check_balance(name)`: Returns the balance of a specific user.
- `deposit(name, amount)`: Deposits an amount into the user's account.
- `withdraw(name, amount)`: Withdraws an amount from the user's account if sufficient funds are available.
- `change_password(name, old_password, new_password)`: Updates the password after verifying the current one.
- `__str__()`: Displays a summary of all users with their details.

