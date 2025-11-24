# Library Management System - User Interaction Layer

# Sample book data: Dictionary with book ID as key, containing title and available copies
books = {
    "y56": {"title": "Harry Potter and the Sorcerer's Stone", "copies": 5},
    "y679": {"title": "The Lord of the Rings", "copies": 3},
    "y78": {"title": "The Hobbit", "copies": 2},
    "y89": {"title": "1984", "copies": 4}
}

# List to store registered users
users = []


def register_user():

    name = input("Enter name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return None

    try:
        age = int(input("Enter age: "))
        if age < 12:
            print("Error: Age must be at least 12.")
            return None
    except ValueError:
        print("Error: Invalid age. Please enter a number.")
        return None

    membership = input("Enter membership type (digital or physical): ").strip().lower()
    if membership not in ["digital", "physical"]:
        print("Error: Membership type must be 'digital' or 'physical'.")
        return None

    user = {"name": name, "age": age, "type": membership, "borrowed": []}
    users.append(user)
    print("User registered successfully.")
    return user


def borrow_book():

    user_name = input("Enter user name: ").strip()
    user = next((u for u in users if u["name"] == user_name), None)
    print( "Harry Potter and the Sorcerer's Stone,ID=y56")
    print("The Lord of the Rings,ID=y679")
    print("The Hobbit,ID=y78")
    print("1984,ID=y89")


    if not user:
        print("Error: User not found.")
        return

    book_id = input("Enter book ID: ").strip()
    if book_id not in books:
        print("Error: Book not found.")
        return

    if books[book_id]["copies"] <= 0:
        print("Error: Book not available.")
        return

    # Borrow the book
    books[book_id]["copies"] -= 1
    user["borrowed"].append(book_id)
    print(f"Book '{books[book_id]['title']}' borrowed successfully.")


def return_book():

    user_name = input("Enter user name: ").strip()
    user = next((u for u in users if u["name"] == user_name), None)
    print("Harry Potter and the Sorcerer's Stone,ID=y56")
    print("The Lord of the Rings,ID=y679")
    print("The Hobbit,ID=y78")
    print("1984,ID=y89")
    if not user:
        print("Error: User not found.")
        return

    book_id = input("Enter book ID to return: ").strip()
    if book_id not in user["borrowed"]:
        print("Error: You haven't borrowed this book.")
        return

    duedays= 5
    dayskept = int(input("How many days did you keep this book for?: "))
    if dayskept > duedays:
        daysover = dayskept - duedays
        sum = daysover * 0.5
        print ("You owe", sum, "£.")

    # Return the book
    user["borrowed"].remove(book_id)
    books[book_id]["copies"] += 1
    print(f"Book '{books[book_id]['title']}' returned successfully.")


def view_member():

    user_name = input("Enter user name: ").strip()
    user = next((u for u in users if u["name"] == user_name), None)
    if not user:
        print("Error: User not found.")
        return

    print("\nMember Details:")
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print(f"Membership Type: {user['type']}")
    print(f"Borrowed Books: {', '.join(user['borrowed']) if user['borrowed'] else 'None'}")


def main_menu():
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Register new member")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View member details")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            view_member()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select 1-5.")


# Run the main menu if this script is executed
if __name__ == "__main__":
    main_menu()