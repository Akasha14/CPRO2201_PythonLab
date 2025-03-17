from pymongo import MongoClient

# MongoDB connection
uri = "mongodb+srv://akasha:Theabk2002@2025python.nnemd.mongodb.net/?retryWrites=true&w=majority&appName=2025Python"
client = MongoClient(uri)

# Select database and collection(table).
db = client["movie_reviews_db"]
collection = db["reviews"]

def add_review():
    # Get user inputs.
    title = input("Enter movie title: ")
    reviewer = input("Enter reviewer name: ")
    rating = int(input("Enter rating (1-10): "))
    review_text = input("Enter review: ")

    # Use user input to create review, then insert into collection.
    review = {
        "title": title,
        "reviewer": reviewer,
        "rating": rating,
        "review_text": review_text
    }
    collection.insert_one(review)
    print("Review added successfully!\n")


def view_reviews():
    # Find all reviews and print each.
    reviews = collection.find()
    for review in reviews:
        print(f"Title: {review['title']}, Reviewer: {review['reviewer']}, Rating: {review['rating']}, Review: {review['review_text']}")
    print()


def update_review():
    # Get user input for title to search, then fields to update.
    title = input("Enter movie title to update: ")
    new_rating = int(input("Enter new rating (1-10): "))
    new_review_text = input("Enter new review text: ")

    # $set for fileds to be updated.
    result = collection.update_one(
        {"title": title},
        {"$set": {"rating": new_rating, "review_text": new_review_text}}
    )

    if result.modified_count:
        print("Review updated successfully!\n")
    else:
        print("No matching review found!\n")


def delete_review():
    # Take user input to search collection and delete_one matching title.
    title = input("Enter movie title to delete: ")
    result = collection.delete_one({"title": title})

    if result.deleted_count:
        print("Review deleted successfully!\n")
    else:
        print("No matching review found!\n")


def search_review():
    # Take user input to search collection for matching title.
    title = input("Enter movie title to search: ")
    review = collection.find_one({"title": title})

    if review:
        print(f"Title: {review['title']}, Reviewer: {review['reviewer']}, Rating: {review['rating']}, Review: {review['review_text']}\n")
    else:
        print("Review not found!\n")
