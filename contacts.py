import os

# List to store contacts
contacts = []

# Function to clear the screen (for better UI)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to add a new contact
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contacts.append(contact)
    print(f"\nContact '{name}' added successfully!")

# Function to view all contacts
def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return

    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

# Function to search contact by name or phone
def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name or phone to search: ").strip().lower()
    found = False

    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\nContact Found:")
            print_contact(contact)
            found = True
            break

    if not found:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if name == contact['name'].lower():
            print("\nLeave field blank to keep current value.")

            new_phone = input(f"New phone ({contact['phone']}): ").strip()
            new_email = input(f"New email ({contact['email']}): ").strip()
            new_address = input(f"New address ({contact['address']}): ").strip()

            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address

            print("\nContact updated successfully!")
            return

    print("Contact not found.")

# Function to delete a contact
def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for contact in contacts:
        if name == contact['name'].lower():
            contacts.remove(contact)
            print(f"Contact '{contact['name']}' deleted successfully.")
            return
    print("Contact not found.")

# Function to display a contact's full details
def print_contact(contact):
    print(f"Name   : {contact['name']}")
    print(f"Phone  : {contact['phone']}")
    print(f"Email  : {contact['email']}")
    print(f"Address: {contact['address']}")

# Main menu function
def main_menu():
    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nGoodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
