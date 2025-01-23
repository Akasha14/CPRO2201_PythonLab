from Book import Book
from LibraryUser import LibraryUser
from MenuMethods import *

# Step 5
while True:
    print("\n--- Library Menu ---")
    print("1. View available books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. View all borrowed books")
    print("5. Exit")
    try:
        option = int(input("\nEnter your choice: "))

        # Use Menu Methods.
        if option == 1:
            view_available_books()
        elif option == 2:
            borrow_book()
        elif option == 3:
            return_book()
        elif option == 4:
            view_borrowed_books()
        elif option == 5:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
