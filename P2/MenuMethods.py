from Book import Book
from LibraryUser import LibraryUser

# Sample books (Step 7). 
library_books = [
    Book("The Hunger Games", "Suzanne Collins", "Fiction"),
    Book("1984", "George Orwell", "Dystopian"),
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
]

# Sample users (Step 7).
user = LibraryUser("Ardan", "A999")
user = LibraryUser("Carter", "A998")


# Step 6.1
def view_available_books():
    print("\nAvailable Books:")
    for book in library_books:
        if book.available:
            print(f"-> {book.title} by {book.author}")

# Step 6.2
def borrow_book():
    # Display list of books that can be borrowed.
    view_available_books()
    title = input("\nEnter the title of the book you want to borrow: ").strip()

    for book in library_books:
        if book.title.lower() == title.lower():
            # Use user's method.
            user.borrow_book(book)
            return

    print(f"The book '{title}' is not available or does not exist.")

# Step 6.4
def view_borrowed_books():
    print("\nBorrowed Books:")
    # Use user's method.
    user.view_borrowed_books()

# Step 6.3
def return_book():
    if user.borrowed_books:
        # Display list of borrowed books that can be returned.
        view_borrowed_books()
        title = input("\nEnter the title of the book you want to return: ").strip()

        for book in user.borrowed_books:
            if book.title.lower() == title.lower():
                # Use user's method.
                user.return_book(book)
                return

        print(f"You haven't borrowed the book titled '{title}'.")
    else:
        print("You have no borrowed books to return.")