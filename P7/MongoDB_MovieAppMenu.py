from CRUD_Operations import *

def main():
    while True:
        print("Welcome to the Movie Reviews App")
        print("1. Add a Review")
        print("2. View All Reviews")
        print("3. Update a Review")
        print("4. Delete a Review")
        print("5. Search for a Movie Review")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_review()
        elif choice == "2":
            view_reviews()
        elif choice == "3":
            update_review()
        elif choice == "4":
            delete_review()
        elif choice == "5":
            search_review()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()