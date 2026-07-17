from datetime import datetime


class Book:

    def __init__(self, title, author, isbn, available=True,book_id=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.book_id = book_id

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {status}"

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
    


