import sqlite3

# Step 1: Function to connect to SQLLite DB.
def connectDB():
    conn = sqlite3.connect("P5/p5_library.db")
    cursor = conn.cursor()

    # Return the connection and cursor.
    return conn, cursor

# Step 2: Function to create tables.
def createTables():
    # Get connection & cursor.
    conn, cursor = connectDB()

    try:
        # Category table.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Category (
                categoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                categoryName TEXT NOT NULL
            )
        ''')
        # Book table.
        cursor.execute('''        
            CREATE TABLE IF NOT EXISTS Book (
                bookID INTEGER PRIMARY KEY AUTOINCREMENT,
                bookName TEXT NOT NULL,
                authorName TEXT,
                yearPublished INTEGER,
                categoryID INTEGER, 
                FOREIGN KEY (categoryID) REFERENCES Category(categoryID)
            )              
        ''')
        # Commit to DB.
        conn.commit()

    except sqlite3.Error as e:
        print(f" Database error: {e}")

    finally:
        # Close connection/cursor.
        cursor.close()
        conn.close() 


# Step 3: Function to insert sample categories.
def insertSampleCategories():
    # Get connection & cursor.
    conn, cursor = connectDB()
    try:
        # Check if there are categories already in the table.
        cursor.execute("SELECT COUNT(*) FROM Category")
        count = cursor.fetchone()[0]
        
        # Only insert if none exist.
        if count == 0:
            categories = [
                ("Fiction",),
                ("Non-Fiction",),
                ("Science",)
            ]
            
            # Executes for each entry in categories list.
            cursor.executemany('''
                INSERT INTO Category (categoryName)
                VALUES (?)
            ''', categories)

            # Commit to DB.
            conn.commit()
            print("Categories inserted.")
        else:
            # Preventing duplicate rows.
            print("Categories already exist. No insertion done.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        # Close connection/cursor.
        cursor.close()
        conn.close() 


# Step 4: Function to insert sample books.
def insertSampleBooks():
    # Get connection & cursor.
    conn, cursor = connectDB()

    try:
        # Check if there are books already in the table.
        cursor.execute("SELECT COUNT(*) FROM Book")
        count = cursor.fetchone()[0]
        
        # Only insert if none exist.
        if count == 0:
            books = [
                ("The Elegant Universe", "Brian Greene", 1999, 3),
                ("The Hunger Games", "Suzanne Collins", 2008, 1),
                ("Educated", "Tara Westover", 2018, 2)
            ]
            
            # Executes for each entry in books list.
            cursor.executemany('''
                INSERT INTO Book (bookName, authorName, yearPublished, categoryID)
                VALUES (?, ?, ?, ?)
            ''', books)

            # Commit to DB.
            conn.commit()
            print("Books inserted.")
        else:
            # Preventing duplicate rows.
            print("Books already exist. No insertion done.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        # Close connection/cursor.
        cursor.close()
        conn.close()

# Step 5: Function to display categories.
def displayCategories():
    # Get connection & cursor.
    conn, cursor = connectDB() 

    try:
        # Fetch and display all categories.
        cursor.execute("SELECT * FROM Category")
        categories = cursor.fetchall()# All rows.

        if categories:
            print("\nCategories:")
            # Loop through each row pulled as tuple (categoryID, categoryName).
            for category in categories:
                print(f"ID: {category[0]}, Name: {category[1]}")
            return categories
        else:
            print("No categories found.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        print()
        # Close connection/cursor.
        cursor.close()
        conn.close() 


# Step 6: Function to display books along with their category names.
def displayBooks():
    # Get connection & cursor.
    conn, cursor = connectDB() 

    try:
        # Fetch books with their category names through table join with categoryID.
        cursor.execute('''
            SELECT Book.bookID, Book.bookName, Book.authorName, Book.yearPublished, Category.categoryName
            FROM Book
            JOIN Category ON Book.categoryID = Category.categoryID
        ''')
        books = cursor.fetchall() # All rows.

        if books:
            print("\nBooks:")
            # Loop through each row pulled as tuple (bookID, bookName, authorName, yearPublished, categoryName).
            for book in books:
                print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Year: {book[3]}, Category: {book[4]}")
        else:
            print("No books found.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        print()
        # Close connection/cursor.
        cursor.close()
        conn.close()