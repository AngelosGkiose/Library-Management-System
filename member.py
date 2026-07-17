class Member:
    def __init__(self, name,email,member_id=None):
        self.name = name
        self.email = email
        self.member_id = member_id

    def __str__(self):
        return f"{self.name} | {self.email} | Borrowed Books:{len(self.borrowed_books)}"

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
            return
        print(f"{self.name} has borrowed :")
        for index,borrowed_book in enumerate(self.borrowed_books):
            print(f"{index+1}. | {borrowed_book.title} ({borrowed_book.isbn})\n")

    def add_borrowed_book(self, book):
        self.borrowed_books.append(book)

    def check_borrowed_books(self):
        if len(self.borrowed_books)==0:
            return True
        else:
            return False

    def has_borrowed(self, book):
        return book in self.borrowed_books

    def remove_borrowed_book(self, book):
        self.borrowed_books.remove(book)

