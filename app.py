import json

FILE_NAME = "books.json"


def show_menu():
    print("""===== Library Management System =====

1. View Books
2. Add Book
3. Delete Book
4. Search Book
5. Borrow Book
6. Return Book
7. Exit""")

class Book:

    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def display_info(self, index):
        status = "Available" if self.available else "Borrowed"
        print(
            f"{index + 1}. Title: {self.title} | "
            f"Author: {self.author} | "
            f"ISBN: {self.isbn} | "
            f"Status: {status}"
        )

    def borrow(self):
        if not self.available:
            return False

        self.available = False
        return True

    def return_book(self):
        if self.available:
            return False

        self.available = True
        return True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["isbn"], data["available"])


class Library:
    def __init__(self):
        self.books = []
    def save_data(self):
        data = [book.to_dict() for book in
                self.books]
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        for index, book in enumerate(self.books):
            book.display_info(index)

    def load_data(self):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book_dict) for book_dict in data]
        except FileNotFoundError:
            self.books = []
        except json.decoder.JSONDecodeError:
            self.books = []

    def add_book(self):
        while True:
            book_title = input("Enter book title: ").strip()

            if not book_title:
                print("Book title cannot be empty.")
                continue

            duplicate_title = any(
                existing_book.title.lower() == book_title.lower()
                for existing_book in self.books
            )

            if duplicate_title:
                print("A book with this title already exists.")
                continue

            book_author = input("Enter book author: ").strip()

            if not book_author:
                print("Book author cannot be empty.")
                continue

            book_isbn = input("Enter book ISBN: ").strip()

            if not book_isbn:
                print("ISBN cannot be empty.")
                continue

            duplicate_isbn = any(
                existing_book.isbn.lower() == book_isbn.lower()
                for existing_book in self.books
            )

            if duplicate_isbn:
                print("A book with this ISBN already exists.")
                continue

            new_book = Book(
                title=book_title,
                author=book_author,
                isbn=book_isbn
            )

            self.books.append(new_book)
            self.save_data()

            print("Book added successfully!")
            return

    def check_book(self):
        while True:
            if not self.books:
                print("No books available.")
                return None
            self.view_books()
            book_title = input("Enter book title: ").strip()
            if not book_title:
                print("Please enter a valid title")
                continue
            for existing_book in self.books:
                if existing_book.title.lower() == book_title.lower():
                    return existing_book
            print("Book not found.")

    def delete_book(self):
        book = self.check_book()

        if book is None:
            return

        self.books.remove(book)
        self.save_data()
        print("Book deleted successfully!")

    def search_book(self):
        if not self.books:
            print("No books found.")
            return

        search_term = input("Enter book title or author: ").strip().lower()

        if not search_term:
            print("Search term cannot be empty.")
            return

        results = []

        for book in self.books:
            if (
                    search_term in book.title.lower()
                    or search_term in book.author.lower()
            ):
                results.append(book)

        if not results:
            print("No matching books found.")
            return

        print("\n===== Search Results =====")

        for index, book in enumerate(results):
            book.display_info(index)

    def borrow_book(self):
        book = self.check_book()

        if book is None:
            return

        if book.borrow():
            self.save_data()
            print("Book borrowed successfully!")
        else:
            print("This book is already borrowed.")

    def return_book(self):
        book = self.check_book()

        if book is None:
            return
        if book.return_book():
            self.save_data()
            print("Book returned successfully!")
        else:
            print("This book is already available.")



def main():
    library = Library()
    library.load_data()
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            library.view_books()
        elif choice == "2":
            library.add_book()
        elif choice == "3":
            library.delete_book()
        elif choice == "4":
            library.search_book()
        elif choice == "5":
            library.borrow_book()
        elif choice == "6":
            library.return_book()
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Please enter a valid choice (1-7)")


if __name__ == '__main__':
    main()