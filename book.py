from datetime import datetime


class Book:

    def __init__(self, title, author, isbn, available=True,borrow_date=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.borrow_date = borrow_date

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {status}"

    def borrow(self):
        if not self.available:
            return False
        self.borrow_date = datetime.now()
        self.available = False
        return True

    def return_book(self):
        if self.available:
            return False
        self.borrow_date =None
        self.available = True
        return True
    
    def days_borrowed(self):
        if self.borrow_date is None:
            return 0
        return (datetime.now() - self.borrow_date).days

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
            "borrow_date": self.borrow_date.isoformat() if self.borrow_date else None
        }

    @staticmethod
    def from_dict(data):
        borrow_date_str = data.get("borrow_date")
        borrow_date = datetime.fromisoformat(borrow_date_str) if borrow_date_str else None
        return Book(data["title"], data["author"], data["isbn"], data["available"], borrow_date)