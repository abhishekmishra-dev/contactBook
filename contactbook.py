class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = self.format_phone(phone)
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

    def format_phone(self, phone):
        # Function to format the phone number (optional)
        return phone

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]
        self.save_contacts()

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def list_contacts(self):
        return self.contacts

    def save_contacts(self):
        with open("contacts.txt", "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone},{contact.email}\n")

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    name, phone, email = line.strip().split(",")
                    self.contacts.append(Contact(name, phone, email))
        except FileNotFoundError:
            pass

def main():
    book = ContactBook()
    book.load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Find Contact")
        print("4. List Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add_contact(Contact(name, phone, email))
            print("Contact added successfully.")
        elif choice == '2':
            name = input("Enter name of the contact to remove: ")
            book.remove_contact(name)
            print("Contact removed successfully.")
        elif choice == '3':
            name = input("Enter name to find: ")
            contact = book.find_contact(name)
            if contact:
                print(contact)
            else:
                print("Contact not found.")
        elif choice == '4':
            contacts = book.list_contacts()
            if contacts:
                for contact in contacts:
                    print(contact)
            else:
                print("No contacts available.")
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
