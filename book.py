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