class User:
    def __init__(self, name, phone, balance, password=None):
        self.name = name  # Public Attribute
        self._phone = phone  # Protected Attribute
        self.__balance = balance  # Private Attribute
        self.__password = password  # Private Attribute

    # Getter for phone
    def get_phone(self):
        return self._phone

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance
    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    # Password verification
    def verify_password(self, password):
        return self.__password == password

    # Change password
    def set_password(self, new_password):
        self.__password = new_password


class BankAccount:
    def __init__(self, users):
        self.users = sorted(users, key=lambda x: x.name)

    # Find user by name
    def __find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    # Check balance
    def check_balance(self, name):
        user = self.__find_user(name)
        if user:
            return f"{user.name}'s balance: ₹{user.get_balance()}"
        return "User not found."

    # Deposit money
    def deposit(self, name, amount):
        if amount <= 0:
            return "Deposit amount must be greater than zero."
        user = self.__find_user(name)
        if user:
            user.set_balance(user.get_balance() + amount)
            return f"₹{amount} deposited successfully. New balance: ₹{user.get_balance()}."
        return "User not found."

    # Withdraw money
    def withdraw(self, name, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        user = self.__find_user(name)
        if user:
            if user.get_balance() >= amount:
                user.set_balance(user.get_balance() - amount)
                return f"₹{amount} withdrawn successfully. Remaining balance: ₹{user.get_balance()}."
            return "Insufficient funds."
        return "User not found."

    # Change password
    def change_password(self, name, old_password, new_password):
        user = self.__find_user(name)
        if user:
            if user.verify_password(old_password):
                user.set_password(new_password)
                return "Password changed successfully."
            return "Incorrect password."
        return "User not found."

    def __str__(self):
        return '\n'.join(
            [f"{user.name} | Phone: {user.get_phone()} | Balance: ₹{user.get_balance()}" for user in self.users]
        )


# Example Usage
users = [
    User("John", "1234567890", 1000, password=8282),
    User("Jane", "0987654321", 2000, password=8281),
    User("Doe1", "9392949294", 3000, password=8234),
    User("Doe2", "1334533430", 4000, password=8080),
]

bank = BankAccount(users)

# Test the User class
print(users[0].name)  # Public
print(users[0]._phone)  #  Protected directly accessed
#print(users[0].get_phone())  # Protected accessed through getter
print(users[0].get_balance())  # Private accessed through getter

# Test the BankAccount class
print(bank.check_balance("John"))
print(bank.deposit("John", 1000))
print(bank.withdraw("John", 500))
print(bank.change_password("John", 8282, 8888))
print(bank)

# Uncommenting the following line will raise an AttributeError
# print(users[0].__password)
