# 2. Simple Data Entry Program

def add_contact(contacts):
    # Get name.
    name = input("Enter contact name: ")
    if name in contacts:
        print(f"Contact with name '{name}' already exists.")
        return
    
    # Use age verifier from part 1.
    try:
        age = int(input("Please entor your age: "))
        if age > 0:
            return age
        else:
            print("Age must be a positive number.")
    except ValueError:
        print("Invalid. Entry must be a number!")
        return

    # Get email.
    email = input("Enter email address: ")

    # Add entry in dictionary with name as key, and a nested dictionary(age, email) as the value.
    contacts[name] = {"age": age, "email": email}

    #Success.
    print(f"Contact '{name}' added successfully!")


def display_all_contacts(contacts):
    # No data.
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        # Name from contact dictionary, details = nested dictionary.
        for name in contacts:
            details = contacts[name]
            print(f"Name: {name}, Age: {details['age']}, Email: {details['email']}")
        print("-------------------")


def main():

    # Dictionary to store contact name and info.
    contacts = {}

    # Menu, loops until exit(3).
    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            display_all_contacts(contacts)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program.
main()
