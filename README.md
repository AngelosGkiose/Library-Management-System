#  Library Management System

A command-line Library Management System built with Python using Object-Oriented Programming.

The application allows users to manage books and library members, borrow and return books, and persist all data using JSON files.

## Features

- View all books
- View all members
- Add new books
- Add new members
- Remove books
- Remove members
- Borrow books
- Return books
- View books borrowed by a specific member
- Search books by title or author
- Track book availability
- Prevent borrowed books from being removed
- Prevent members with borrowed books from being removed
- Prevent duplicate ISBNs
- Prevent duplicate member IDs
- Persistent storage using JSON files
- Input validation and error handling

## Object-Oriented Design

The project uses three main classes:

### Book

Represents a book in the library.

Each book contains:

- Title
- Author
- ISBN
- Availability status

The class also handles:

- Borrowing a book
- Returning a book
- Converting a book to and from a dictionary

### Member

Represents a library member.

Each member contains:

- Name
- Member ID
- A list of borrowed books

The class also handles:

- Adding borrowed books
- Removing returned books
- Checking whether a member borrowed a specific book
- Displaying borrowed books

### Library

Manages the complete library system.

It handles:

- Books
- Members
- Borrowing and returning
- Searching
- Adding and removing data
- Application rules and validation


## Technologies Used

- Python 3
- Object-Oriented Programming
- JSON
- File handling
- Type hints

## Data Storage

Book data is stored in:

```text
books.json
```

Member data is stored in:

```text
members.json
```
Borrowed books are stored by ISBN and reconnected to their corresponding `Book` objects when the program starts.

## How to Run

Clone the repository:

```bash
git clone https://github.com/AngelosGkiose/library-management-system.git
```

Move into the project directory:

```bash
cd library-management-system
```

Run the application:

```bash
python main.py
```

## Menu

```text
===== Library Management System =====

1. View All Books
2. View All Members
3. Add Book
4. Add Member
5. Borrow Book
6. Return Book
7. View Member's Borrowed Books
8. Remove Book
9. Remove Member
10. Exit
```

## Example Book

```text
1. Title: Atomic Habits | Author: James Clear | ISBN: 9780735211292 | Status: Available
```

## Example Member

```text
1. Name: John Smith | Member ID: M001 | Borrowed Books: 2
```

## What I Learned

This project helped me practice:

- Classes and objects
- Encapsulation
- Object relationships
- Lists of objects
- Serialization and deserialization
- JSON persistence
- Type hints
- File organization with modules
- Input validation
- Searching and filtering
- Business rules
- Code reuse
- Separation of responsibilities

## Future Improvements

- Replace JSON storage with SQLite
- Add book categories
- Add borrowing dates
- Add return deadlines
- Add late return penalties
- Add multiple copies of the same book
- Add member contact information
- Add automated tests with `pytest`
- Add a graphical or web interface