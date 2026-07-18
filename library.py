from datetime import date

from book import Book
from database import Database
from loan import Loan
from member import Member


MAX_DAYS = 14
FINE_PER_DAY = 0.50



class Library:
    def __init__(self):
        self.database=Database()

    def has_books(self):
        books = self.database.get_all_books()
        if not books:
            print("No books available.")
            return False
        for index, book in enumerate(books):
            print(f"{index + 1}. {book}")
        return True

    def has_members(self):
        members = self.database.get_all_members()
        if not members:
            print("No members available.")
            return False
        return True

    def get_member_from_user(self):
        while True:
            member_email = input(
                "Enter member email (0 to cancel): "
            ).strip().lower()
            if member_email == "0":
                return None
            if not member_email:
                print("Member email cannot be empty.")
                continue
            member = self.database.get_member_by_email(member_email)
            if member is None:
                print("Member was not found.")
                continue
            return member

    def get_book_from_user(self):
        while True:
            book_isbn = input(
                "Enter book ISBN (0 to cancel): "
            ).strip()
            if book_isbn == "0":
                return None
            if not book_isbn:
                print("ISBN cannot be empty.")
                continue
            book = self.database.get_book_by_isbn(book_isbn)
            if book is None:
                print("Book was not found.")
                continue
            return book

    def view_members(self):
        members=self.database.get_all_members()
        if not members:
            print("No members available.")
            return
        for index, member in enumerate(members):
            print(f"{index+1}. {member}")

    def add_member(self):
        while True:
            member_name=input("Enter member name: ").strip()
            if not member_name:
                print("Member name cannot be empty.")
                continue
            member_email=input("Enter member email: ").strip().lower()
            if not member_email:
                print("Member email cannot be empty.")
                continue
            if "@" not in member_email or "." not in member_email:
                print("Please enter a valid email address.")
                continue
            old_member=self.database.get_member_by_email(member_email)
            if old_member:
                print("A member with this email already exists.")
                continue
            new_member=Member(member_name,member_email)
            completed=self.database.add_member(new_member)
            if completed:
                print("Member added successfully!")
            else:
                print("Member did not add successfully!")
            return

    def view_members_books(self):
        members=self.database.get_all_members()
        if not members:
            print("No members available.")
            return
        member = self.get_member_from_user()
        if member is None:
            return
        member_borrowed_books=self.database.get_member_borrowed_book(member)
        if not member_borrowed_books:
            print(f"{member.name} has no borrowed books.")
            return
        print(f"{member.name} has borrowed :")
        for index, borrowed_book in enumerate(member_borrowed_books):
            print(f"{index + 1}. | {borrowed_book.title} ({borrowed_book.isbn})\n")

    def remove_member(self):
        members=self.database.get_all_members()
        if not members:
            print("No members available.")
            return
        member = self.get_member_from_user()
        if member is None:
            return
        if self.database.has_no_borrowed_books(member):
            completed=self.database.remove_member(member)
            if completed:
                print("Member removed successfully!")
            else:
                print("Member did not remove successfully!")
        else:
            print("Cannot remove this member. They still have borrowed books.")

    def view_books(self):
        books=self.database.get_all_books()
        if not books:
            print("No books available.")
            return
        for index, book in enumerate(books):
            print(f"{index+1}. {book}")

    def add_book(self):
        while True:
            book_title = input("Enter book title: ").strip()
            if not book_title:
                print("Book title cannot be empty.")
                continue
            book_author = input("Enter book author: ").strip()
            if not book_author:
                print("Book author cannot be empty.")
                continue
            book_isbn = input("Enter book ISBN: ").strip()
            if not book_isbn:
                print("ISBN cannot be empty.")
                continue
            existing_book=self.database.get_book_by_isbn(book_isbn)
            if existing_book:
                print("A book with this ISBN already exists.")
                continue
            new_book = Book(
                title=book_title,
                author=book_author,
                isbn=book_isbn
            )
            completed=self.database.add_book(new_book)
            if completed:
                print("Book added successfully!")
            else:
                print("Book did not add successfully!")
            return


    def delete_book(self):
        if not self.has_books():
            return
        book = self.get_book_from_user()
        if book is None:
            return
        if not book.available:
            print("Cannot remove this book. It is currently borrowed.")
            return
        completed=self.database.remove_book(book)
        if completed:
            print("Book deleted successfully!")
        else:
            print("Book did not delete successfully!")

    def borrow_book(self):
        if not self.has_books():
            return
        if not self.has_members():
            return
        member = self.get_member_from_user()
        if member is None:
            return
        book = self.get_book_from_user()
        if book is None:
            return
        if book.borrow():
            loan=Loan(book.book_id,member.member_id,date.today().isoformat())
            completed=self.database.borrow_book(loan)
            if completed:
                print(f"Book {book.title} borrowed successfully by {member.name}!")
            else:
                print("Book did not borrow successfully!")
                book.available = True
        else:
            print("This book is already borrowed.")

    def return_book(self):
        if not self.has_books():
            return
        if not self.has_members():
            return
        member = self.get_member_from_user()
        if member is None:
            return
        book = self.get_book_from_user()
        if book is None:
            return
        if not self.database.has_borrowed(member,book):
            print("This book isn't yours.")
            return
        loan=self.database.get_loan(member,book)
        if loan is None:
            print("Loan was not found.")
            return
        days = loan.days_borrowed()
        returned =book.return_book()
        if  not returned :
            print("This book isn't borrowed yet.")
            return
        completed=self.database.return_book(loan)
        if completed:
            print(f"Book {book.title} returned successfully by {member.name}!")
        else:
            print("Book could not be returned.")
            book.available = False
            return

        if days > MAX_DAYS:
            overdue_days = days - MAX_DAYS
            fine = overdue_days * FINE_PER_DAY
            print(f"Late return: {overdue_days} days overdue. Fine: €{fine:.2f}")

    def close(self):
        self.database.close()