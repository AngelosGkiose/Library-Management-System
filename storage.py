import json

from book import Book
from member import Member


BOOKS_FILE = "books.json"
MEMBERS_FILE = "members.json"


def save_books(books):
    data = [book.to_dict() for book in books]

    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
        )


def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            Book.from_dict(book_data)
            for book_data in data
        ]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Invalid books JSON file. Starting with an empty book list.")
        return []


def save_members(members):
    data = [member.to_dict() for member in members]

    with open(MEMBERS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,   
        )


def load_members(books):
    try:
        with open(MEMBERS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        members = [
            Member.from_dict(member_data)
            for member_data in data
        ]

        for member_data, member in zip(data, members):
            borrowed_isbns = member_data.get("borrowed_books", [])

            for isbn in borrowed_isbns:
                book = find_book_by_isbn(books, isbn)

                if book is not None:
                    member.add_borrowed_book(book)

        return members

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Invalid members JSON file. Starting with an empty member list.")
        return []


def find_book_by_isbn(books, isbn):
    for book in books:
        if book.isbn.lower() == isbn.lower():
            return book

    return None