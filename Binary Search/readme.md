# Binary Search Contact Search 

This folder contains an example of implementing a **Binary Search Algorithm** to search for a contact in a list of contacts. The repository is part of the ` Reallife-DataStructure` series, focusing on practical use cases of data structures.

---

## Features

- **Class-Based Design**:
  - `User`: Represents a contact with `name` and `phone` attributes.
  - `BinarySearchContact`: Encapsulates the binary search functionality for a sorted list of `User` objects.

- **Key Functionalities**:
  - Automatically sorts the contact list by name.
  - Efficiently searches for a contact using Binary Search.
  - Provides meaningful feedback when a contact is not found.

---

## Code Explanation

### Classes
1. **`User` Class**:
   - Represents an individual contact.
   - Overrides the `__str__` method for a clean representation.

    ```python
    class User:
        def __init__(self, name, phone):
            self.name = name
            self.phone = phone

        def __str__(self):
            return f'{self.name} {self.phone}'
    ```

2. **`BinarySearchContact` Class**:
   - Manages a sorted list of `User` objects.
   - Implements the binary search algorithm to find a contact by name.

    ```python
    class BinarySearchContact:
        def __init__(self, contacts):
            self.contacts = contacts
            self.contacts.sort(key=lambda x: x.name)

        def search(self, name):
            left = 0
            right = len(self.contacts) - 1
            while left <= right:
                mid = (left + right) // 2
                mid_value = self.contacts[mid]
                if mid_value.name == name:
                    return mid_value
                if mid_value.name < name:
                    left = mid + 1
                else:
                    right = mid - 1
            return 'Contact not found'
    ```

---

## Example Usage

Here's an example demonstrating how to use the `BinarySearchContact` class:

```python
contacts = [
    User('John', '1234567890'),
    User('Jane', '0987654321'),
    User('Doe', '1234567890')
]

search = BinarySearchContact(contacts)

# Search for a contact
result = search.search('Jane')
print(result)  # Output: Jane 0987654321

# Search for a non-existent contact
result = search.search('Alice')
print(result)  # Output: Contact not found
```