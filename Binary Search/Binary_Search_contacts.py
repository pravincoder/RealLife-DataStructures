# Create a Binary Search Algo to search for a contact in a list of contacts
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return f'{self.name} {self.phone}'
    
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

contacts = [User('John', '1234567890'), User('Jane', '0987654321'), User('Doe', '1234567890'), User('Doe', '1234567890')]
search = BinarySearchContact(contacts)

print(search.search('Jane'))

print(search.search('Alice'))