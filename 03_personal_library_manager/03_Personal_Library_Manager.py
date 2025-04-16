import os
import json

data_file = "library.txt"

# Load library from file
def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)

# Display Menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a Book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Try again.")
        return
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

# Remove a Book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a Book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        search_title = input("Enter the title: ").strip().lower()
        matches = [book for book in library if search_title in book["title"].lower()]
    elif choice == "2":
        search_author = input("Enter the author: ").strip().lower()
        matches = [book for book in library if search_author in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if matches:
        print("\nMatching Books:")
        for idx, book in enumerate(matches, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

# Display All Books
def display_books(library):
    if not library:
        print("Your library is empty.")
        return

    print("\nYour Library:")
    for idx, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Display Statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("Your library is empty.")
        return
    read_count = sum(1 for book in library if book["read"])
    percentage = (read_count / total) * 100
    print(f"\nTotal books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

# Main Function
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
