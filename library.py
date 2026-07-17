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
            member_email=input("Enter member email: ").strip()
            if not member_email:
                print("Member email cannot be empty.")
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
            book=self.database.get_book_by_title(book_title)
            if  book:
                print("Book with this title already exists.")
                continue
            book_author = input("Enter book author: ").strip()
            if not book_author:
                print("Book author cannot be empty.")
                continue
            book_isbn = input("Enter book ISBN: ").strip()
            if not book_isbn:
                print("ISBN cannot be empty.")
                continue
            book_ISBN=self.database.get_book_by_isbn(book_isbn)
            if book_ISBN:
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

        if not book.available:
            print("Cannot remove this book. It is currently borrowed.")
            return
        self.books.remove(book)
        save_books(self.books)
        print("Book deleted successfully!")

    def borrow_book(self):
        self.view_books()
        member_email = input("Enter member email: ").strip()
        if not member_email:
            print("Please enter a valid member email")
            return
        member=self.database.get_member_by_email(member_email)
        if member is None:
            return
        book_isbn = input("Enter book ISBN: ").strip()
        if not book_isbn:
            print("Please enter a valid ISBN")
            return
        book=self.database.get_book_by_isbn(book_isbn)
        if book is None:
            return
        if book.borrow():
            loan=Loan(book.book_id,member.member_id,date.today().isoformat())
            completed=self.database.borrow_book(loan)
            if completed:
                print(f"Book {book.title} borrowed successfully by {member.name}!")
            else:
                print("Book did not borrow successfully!")
        else:
            print("This book is already borrowed.")

    def return_book(self):
        member_email = input("Enter member email: ").strip()
        if not member_email:
            print("Please enter a valid member email")
            return
        member = self.database.get_member_by_email(member_email)
        if member is None:
            return
        book_isbn = input("Enter book ISBN: ").strip()
        if not book_isbn:
            print("Please enter a valid ISBN")
            return
        book=self.database.get_book_by_isbn(book_isbn)
        if book is None:
            return
        if not self.database.has_borrowed(member,book):
            print("This book isn't yours.")
            return
        loan=self.database.get_loan(member,book)
        if loan is None:
            return
        days = loan.days_borrowed()

        borrowed=book.return_book()
        if  not borrowed:
            print("This book isn't borrowed yet.")
            return
        completed=self.database.return_book(loan)
        if completed:
            print(f"Book {book.title} returned successfully by {member.name}!")
        else:
            print("Book did not return successfully!")

        if days > MAX_DAYS:
            overdue_days = days - MAX_DAYS
            fine = overdue_days * FINE_PER_DAY
            print(f"Late return: {overdue_days} days overdue. Fine: €{fine:.2f}")