
from book import Book
from member import Member
from storage import (
    load_books,
    load_members,
    save_books,
    save_members,
)

MAX_DAYS = 14
FINE_PER_DAY = 0.50
BOOKS_FILE = "books.json"
MEMBERS_FILE = "members.json"


class Library:
    def __init__(self):
        self.books = load_books()
        self.members = load_members(self.books)
    def view_members(self):
        if not self.members:
            print("No members available.")
            return
        for index, member in enumerate(self.members):
            print(f"{index+1}. {member}")

    def add_member(self):
        while True:
            member_name=input("Enter member name: ").strip()
            if not member_name:
                print("Member name cannot be empty.")
                continue
            member_id = input("Enter member id: ").strip()
            if not member_id:
                print("Member id cannot be empty.")
                continue
            duplicate=any(existing_member.member_id.lower()==member_id.lower() for existing_member in self.members)
            if duplicate:
                print("A member with this id already exists.")
                continue
            member=Member(member_name,member_id)
            self.members.append(member)
            print("Member added successfully!")
            save_members(self.members)
            return

    def view_members_books(self):
        if not self.members:
            print("No members available.")
            return

        member = self.check_member_id()

        if member is None:
            return

        member.display_borrowed_books()

    def remove_member(self):
        self.view_members()
        member=self.check_member_id()
        if member is None:
            return
        if member.check_borrowed_books():
            self.members.remove(member)
            save_members(self.members)
            print("Member removed successfully!")
        else:
            print("Cannot remove this member. They still have borrowed books.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        for index, book in enumerate(self.books):
            print(f"{index+1}. {book}")

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
            save_books(self.books)

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

    def check_book_isbn(self):
        while True:
            if not self.books:
                print("No books available.")
                return None
            book_isbn = input("Enter book ISBN: ").strip()
            if not book_isbn:
                print("Please enter a valid ISBN")
                continue
            for existing_book in self.books:
                if existing_book.isbn.lower()==book_isbn.lower():
                    return existing_book
            print("ISBN not found.")


    def check_member_id(self):
        while True:
            if not self.members:
                print("No members available.")
                return None
            member_id = input("Enter member id: ").strip()
            if not member_id:
                print("Member id cannot be empty.")
                continue
            for existing_member in self.members:
                if existing_member.member_id.lower()==member_id.lower():
                    return existing_member
            print("Member id not found")

    def delete_book(self):
        book = self.check_book()

        if book is None:
            return

        if not book.available:
            print("Cannot remove this book. It is currently borrowed.")
            return
        self.books.remove(book)
        save_books(self.books)
        print("Book deleted successfully!")

    def borrow_book(self):
        self.view_books()
        member=self.check_member_id()
        if member is None:
            return
        book = self.check_book_isbn()

        if book is None:
            return

        if book.borrow():
            save_books(self.books)
            member.add_borrowed_book(book)
            save_members(self.members)
            print(f"Book {book.title} borrowed successfully by {member.name}!")
        else:
            print("This book is already borrowed.")

    def return_book(self):
        self.view_books()
        member=self.check_member_id()
        if member is None:
            return
        book = self.check_book_isbn()
        if book is None:
            return
        if not member.has_borrowed(book):
            print("This book isn't yours.")
            return
        book.return_book()
        member.remove_borrowed_book(book)
        save_books(self.books)
        save_members(self.members)
        print(f"Book {book.title} returned successfully by {member.name}!")