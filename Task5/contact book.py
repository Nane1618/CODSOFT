class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add(self, name, phone_number, email, address):
        self.contacts[name] = {
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added successfully!")

    def view_contact_list(self):
        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"{name}: {details['phone_number']}")

    def search(self, search_term):
        search_results = []
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone_number']:
                search_results.append((name, details))
        return search_results

    def update(self, name, new_phone_number, new_email, new_address):
        if name in self.contacts:
            self.contacts[name]['phone_number'] = new_phone_number
            self.contacts[name]['email'] = new_email
            self.contacts[name]['address'] = new_address
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found")

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found")

# Sample usage:
contact_manager = ContactManager()

while True:
    print("\ncontacts arrangement system")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact_manager.add(name, phone_number, email, address)

    elif choice == '2':
        contact_manager.view_contact_list()

    elif choice == '3':
        search_term = input("Enter name or phone number to search: ")
        search_results = contact_manager.search_contact(search_term)
        if search_results:
            print("Search Results:")
            for name, details in search_results:
                print(f"{name}: {details['phone_number']}")
        else:
            print("No contacts found.")

    elif choice == '4':
        name = input("Enter name of the contact to update: ")
        new_phone_number = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")
        contact_manager.update(name, new_phone_number, new_email, new_address)

    elif choice == '5':
        name = input("Enter name of the contact to delete: ")
        contact_manager.delete(name)

    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
