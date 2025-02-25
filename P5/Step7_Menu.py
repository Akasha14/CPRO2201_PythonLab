import sqlite3
from Step1to6_DB_Functions import *
from Step7_AddUpdateDelete import *

# Step 7:  Interactive menu-driven system.
def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View all categories")
        print("2. View all books")
        print("3. Add a new category")
        print("4. Add a new book")
        print("5. Update a category")
        print("6. Update a book")
        print("7. Delete a book")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            displayCategories()
        elif choice == "2":
            displayBooks()
        elif choice == "3":
            addCategory()
        elif choice == "4":
            addBook()
        elif choice == "5":
            updateCategory()
        elif choice == "6":
            updateBook()
        elif choice == "7":
            deleteBook()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

# Run the menu.
menu()