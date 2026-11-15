# Library Management System

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.issued_to = []


class Library:
    def __init__(self):
        self.books = {}

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be positive!")
                return

        except ValueError:
            print("Please enter a valid number!")
            return

        self.books[book_id] = Book(book_id, title, author, quantity)
        print("Book added successfully!")

    # View All Books
    def view_books(self):
        if not self.books:
            print("No books available!")
            return

        for book in self.books.values():
            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Available Quantity:", book.quantity)

    # Search Book
    def search_book(self):
        search = input("Enter Book ID or Title: ").lower()

        found = False

        for book in self.books.values():
            if search == book.book_id.lower() or search in book.title.lower():
                print("\nBook ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Quantity:", book.quantity)
                found = True

        if not found:
            print("Book not found!")

    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        if book.quantity == 0:
            print("Book is not available!")
            return

        student = input("Enter Student Name: ")

        book.quantity -= 1
        book.issued_to.append(student)

        print("Book issued successfully!")
        print("Available Quantity:", book.quantity)

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]
        student = input("Enter Student Name: ")

        if student not in book.issued_to:
            print("No issued record found for this student!")
            return

        book.issued_to.remove(student)
        book.quantity += 1

        print("Book returned successfully!")
        print("Available Quantity:", book.quantity)

    # Delete Book
    def delete_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        if book.issued_to:
            print("Cannot delete! Book is currently issued.")
            return

        del self.books[book_id]
        print("Book deleted successfully!")

    # View Issued Books
    def view_issued_books(self):
        found = False

        for book in self.books.values():
            for student in book.issued_to:
                print("\nBook ID:", book.book_id)
                print("Book Title:", book.title)
                print("Student Name:", student)
                found = True

        if not found:
            print("No books are currently issued!")


# Main Program
library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        library.view_issued_books()

    elif choice == "8":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")