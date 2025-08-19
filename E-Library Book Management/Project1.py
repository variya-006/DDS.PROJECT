import os

BOOKS_FILE = "books.txt"

def load_books():
    books = []
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 4:
                    book = {
                        "id": data[0],
                        "title": data[1],
                        "author": data[2],
                        "year": data[3]
                    }
                    books.append(book)
    return books

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        for book in books:
            f.write(f"{book['id']},{book['title']},{book['author']},{book['year']}\n")

def add_book():
    id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = input("Enter Year of Publication: ")

    books = load_books()

    # Check for duplicate ID
    if any(book["id"] == id for book in books):
        print("Book ID already exists!")
        return

    books.append({"id": id, "title": title, "author": author, "year": year})
    save_books(books)
    print("Book added successfully!\n")

def view_books():
    books = load_books()
    if not books:
        print("No books found.\n")
        return
    print("\nAvailable Books:")
    print("{:<10} {:<30} {:<20} {:<6}".format("ID", "Title", "Author", "Year"))
    print("-"*70)
    for book in books:
        print("{:<10} {:<30} {:<20} {:<6}".format(book['id'], book['title'], book['author'], book['year']))
    print()

def search_book():
    search_title = input("Enter the book title to search: ").lower()
    books = load_books()
    found = False
    for book in books:
        if search_title in book['title'].lower():
            if not found:
                print("\nSearch Results:")
                print("{:<10} {:<30} {:<20} {:<6}".format("ID", "Title", "Author", "Year"))
                print("-"*70)
                found = True
            print("{:<10} {:<30} {:<20} {:<6}".format(book['id'], book['title'], book['author'], book['year']))
    if not found:
        print("No book found with that title.\n")

def delete_book():
    book_id = input("Enter the Book ID to delete: ")
    books = load_books()
    new_books = [book for book in books if book['id'] != book_id]
    
    if len(new_books) == len(books):
        print("Book not found.\n")
    else:
        save_books(new_books)
        print("Book deleted successfully!\n")

def main_menu():
    while True:
        print("=== E-Library Book Management ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if _name_ == "_main_":
    main_menu()
