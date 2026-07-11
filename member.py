class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def display_info(self, index):
        print(f"{index + 1}. Name: {self.name} | {self.member_id} | Borrowed Books: {len(self.borrowed_books)}")

    def to_dict(self):
        return{"name":self.name,"member_id":self.member_id,"borrowed_books": [book.isbn for book in self.borrowed_books]}

    @staticmethod
    def from_dict(data):
        return Member(data["name"], data["member_id"])

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

