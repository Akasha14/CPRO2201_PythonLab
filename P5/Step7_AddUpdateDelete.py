import sqlite3
from Step1to6_DB_Functions import *

# Step 7.1: Function to add a new category.
def addCategory():
    # Get connection & cursor.
    conn, cursor = connectDB() 
    
    # For usability.
    displayCategories()

    try:
        # Get user input and use for insert.
        category_name = input("Enter the name of the new category: ")
        cursor.execute("INSERT INTO Category (categoryName) VALUES (?)", (category_name,))
        # Commit to DB.
        conn.commit()
        print(f"Category '{category_name}' added successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        # Close connection/cursor.
        cursor.close()
        conn.close()


# Step 7.2: Function to add a new book.
def addBook():
    # Get connection & cursor.
    conn, cursor = connectDB() 
    
    try:
        # Get user input for each individual field required.
        book_name = input("Enter the name of the book: ")
        author_name = input("Enter the author's name(optional): ")
        year_published = int(input("Enter the year the book was published(optional): "))
        category_id = int(input("Enter the category ID for the book: "))
        
        # Use user inputs for insert.
        cursor.execute('''
            INSERT INTO Book (bookName, authorName, yearPublished, categoryID)
            VALUES (?, ?, ?, ?)
        ''', (book_name, author_name, year_published, category_id))
        # Commit to DB.
        conn.commit()
        print(f"Book '{book_name}' added successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # Close connection/cursor.
        cursor.close()
        conn.close()


# Step 7.3: Function to update a category.
def updateCategory():
    # Get connection & cursor.
    conn, cursor = connectDB() 

    # For usability.
    displayCategories()

    # Get categories.
    cursor.execute("SELECT categoryID, categoryName FROM Category")
    categories = cursor.fetchall()

    try:
        # Get user input (categoryID).
        category_id = int(input("Enter the ID of the category you want to update: "))

        # Check if category ID exists
        selected_category = None
        for cat in categories:
            # If id from db equal to user input.
            if cat[0] == category_id:
                selected_category = cat
                break 
        # Category wasn't found.
        if not selected_category:
            print("Invalid category ID. Please try again.")
            return

        # Get updated name from user.
        new_name = input(f"Enter new category name:")
        # Update statement with user inputs.
        cursor.execute("UPDATE Category SET categoryName = ? WHERE categoryID = ?", (new_name, category_id))
        # Commit to DB.
        conn.commit()
        print("Category updated successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the category ID.")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
    finally:
        conn.close() # Close connection.


# Step 7.4: Function to update a book.
def updateBook():
    # Get connection & cursor.
    conn, cursor = connectDB() 

    # For usability.
    displayCategories()
    displayBooks()

    # Get books.
    cursor.execute("SELECT bookID, bookName, authorName, yearPublished, categoryID FROM Book")
    books = cursor.fetchall()

    try:
        # Get user input (bookID).
        book_id = int(input("Enter the ID of the book you want to update: "))

        # Check if book ID exists
        selected_book = None
        for book in books:
            # If id from db equal to user input.
            if book[0] == book_id:
                selected_book = book
                break 
        # Book wasn't found.
        if not selected_book:
            print("Invalid book ID. Please try again.")
            return

        # Get updated input from user or default.
        new_title = input(f"Enter new title for the book (Leave blank to keep '{selected_book[1]}'): ") or selected_book[1]
        new_author = input(f"Enter new author for the book (Leave blank to keep '{selected_book[2]}'): ") or selected_book[2]
        new_year = input(f"Enter new publishing year for the book (Leave blank to keep '{selected_book[3]}'): ") or selected_book[3]
        new_category = input(f"Enter new category for the book (Leave blank to keep '{selected_book[4]}'): ") or selected_book[4]

        # Update statement with user inputs.
        cursor.execute("""
            UPDATE Book SET bookName = ?, authorName = ?, yearPublished = ?, categoryID = ? WHERE bookID = ?
        """, (new_title, new_author, new_year, new_category, book_id))

        # Commit to DB.
        conn.commit()
        print("Book updated successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the book ID.")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
    finally:
        conn.close() # Close connection.


# Step 7.5: Function to delete a book.
def deleteBook():
    # Get connection & cursor.
    conn, cursor = connectDB() 

    displayBooks()

    # Get books.
    cursor.execute("SELECT bookID, bookName, authorName, yearPublished, categoryID FROM Book")
    books = cursor.fetchall()

    try:
        # Get user input (bookID).
        book_id = int(input("Enter the ID of the book you want to DELETE: "))

        # Check if book ID exists
        selected_book = None
        for book in books:
            # If id from db equal to user input.
            if book[0] == book_id:
                selected_book = book
                break 
        # Book wasn't found.
        if not selected_book:
            print("Invalid book ID. Please try again.")
            return

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete the book '{selected_book[1]}'? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Book deletion cancelled.")
            return

        # Delete statement with user input.
        cursor.execute("DELETE FROM Book WHERE bookID = ?", (book_id,))

        # Commit to DB.
        conn.commit()
        print("Book deleted successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the book ID.")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
    finally:
        conn.close() # Close connection.