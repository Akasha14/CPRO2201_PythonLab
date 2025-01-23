from Book import Book

# Step 2
class LibraryUser:

    # Constructor.
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []  # List.

    # Step 4.1
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed {book.title}.")
        else:
            print(f"{book.title} is unavailable.")

    # Step 4.2
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned {book.title}.")
        else:
            print(f"{self.name} can't return {book.title} (not borrowed).")

    # Step 4.3
    def view_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")

            # Loop through list of books to print.
            for book in self.borrowed_books:
                print(f"-> {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")
        