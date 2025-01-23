
# Step 1
class Book:

    # Constructor.
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    # Step 3.1
    def borrow(self):
        if self.available:
            self.available = False
        else:
            print(f"{self.title} is in use!")

    # Step 3.2
    def return_book(self):
        if not self.available:
            self.available = True
        else:
            print("Book was never taken!")

    # Step 3.3
    def display_info(self):
        # Status to print.
        availability_status = "Available" if self.available else "Not Available"

        print(f"{self.title}, written by: {self.author}, {self.genre}. Availability: {availability_status}")