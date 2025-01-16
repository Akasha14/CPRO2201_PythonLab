# 4. File Storage and Retrieval.

FILENAME = "saved_contacts.txt"

def save_contacts(contacts):
    # Open in write(w) mode.
    with open(FILENAME, "w") as file:
        # Loop all contacts to be saved.
        for name, age in contacts.items():
            # Save as name, age.
            file.write(f"{name},{age}\n")
    print("Contacts saved successfully!")


def load_contacts():
    # Dictionary to store items from file.
    contacts = {}
    try:
        # Open in read(r) mode.
        with open(FILENAME, "r") as file:
            # Save each line into dictionary.
            for line in file:
                name, age = line.split(",")
                contacts[name] = int(age)
        print("Contacts loaded successfully!")
    except FileNotFoundError:
        print("No contacts loaded. File does not exist.")
    return contacts

# Much same from part 2.
def display_all_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
    else:
        print("\n--- Contact List ---")
        for name, age in contacts.items():
            print(f"Name: {name}, Age: {age}")
        print("---------------------")

# Much same from part 2.
def add_contact(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print(f"Contact with name '{name}' already exists.")
        return

    try:
        age = int(input("Enter age: "))
        if age <= 0:
            print("Age must be a positive number.")
            return
    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    contacts[name] = age
    print(f"Contact '{name}' added successfully!")


def main():
    contacts = load_contacts()

    # Menu, loops until exit(4).
    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Save Contacts to File")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            display_all_contacts(contacts)
        elif choice == "3":
            save_contacts(contacts)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
