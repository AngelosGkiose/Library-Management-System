#  Library Management System

A command-line Library Management System built with Python using Object-Oriented Programming.

The application manages books, library members, borrowing, returns, borrowing dates, and late-return fines. All data is stored locally using JSON files.

## Features

### Book Management

- View all books
- Add new books
- Remove books
- Search books by title or author
- Track book availability
- Prevent duplicate ISBNs
- Prevent borrowed books from being removed

### Member Management

- View all members
- Add new members
- Remove members
- Prevent duplicate member IDs
- Prevent members with borrowed books from being removed
- View all books borrowed by a specific member

### Borrowing System

- Borrow available books
- Return borrowed books
- Associate borrowed books with specific members
- Prevent already borrowed books from being borrowed again
- Prevent members from returning books they did not borrow

### Borrowing Dates

- Store the exact date when a book is borrowed
- Display the borrowing date
- Show how many days a member has kept each borrowed book
- Remove the borrowing date when the book is returned

### Late Return Fines

- Books can be borrowed for up to 14 days without a fine
- Late days are calculated automatically
- A fine is calculated for each overdue day
- Fine information is displayed when the book is returned

Example:

```text
Book "1984" returned successfully by John Smith!
Late return: 5 days overdue.
Fine: €2.50
```

### Persistent Storage

- Books are stored in `books.json`
- Members are stored in `members.json`
- Borrowed books are stored using their ISBN
- Borrowed book relationships are restored when the program starts
- Borrowing dates are converted to strings for JSON storage and restored as `datetime` objects when loaded

## Object-Oriented Design

The project is organized around three main classes.

### `Book`

Represents a book in the library.

Each book contains:

- Title
- Author
- ISBN
- Availability status
- Borrowing date

Main responsibilities:

- Borrowing a book
- Returning a book
- Tracking its borrowing date
- Calculating how many days it has been borrowed
- Converting itself to and from a dictionary
- Providing a readable string representation through `__str__`

Example:

```python
book = Book("1984", "George Orwell", "111")
print(book)
```

Output:

```text
Title: 1984 | Author: George Orwell | ISBN: 111 | Status: Available
```

### `Member`

Represents a library member.

Each member contains:

- Name
- Member ID
- List of borrowed books

Main responsibilities:

- Adding a borrowed book
- Removing a returned book
- Checking whether a specific book was borrowed
- Displaying borrowed books
- Providing a readable string representation through `__str__`

Example:

```python
member = Member("John Smith", "M001")
print(member)
```

Output:

```text
Name: John Smith | Member ID: M001 | Borrowed Books: 0
```

### `Library`

Manages the complete library system.

Main responsibilities:

- Managing books and members
- Searching books
- Borrowing and returning books
- Removing books and members
- Enforcing application rules
- Saving changes through the storage module

## Project Structure

```text
Library-Management-System/
│
├── main.py
├── library.py
├── book.py
├── member.py
├── storage.py
├── books.json
├── members.json
├── README.md
└── .gitignore
```

### File Responsibilities

- `main.py` — application menu and program entry point
- `library.py` — main library operations and business rules
- `book.py` — `Book` class
- `member.py` — `Member` class
- `storage.py` — JSON loading and saving
- `books.json` — stored book data
- `members.json` — stored member data

## Technologies Used

- Python 3
- Object-Oriented Programming
- JSON
- File handling
- Type hints
- Serialization and deserialization

## Installation

Clone the repository:

```bash
git clone https://github.com/AngelosGkiose/Library-Management-System.git
```

Move into the project directory:

```bash
cd Library-Management-System
```

Run the application:

```bash
python main.py
```

No external packages are required.

## Application Menu

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

## Example Book Output

```text
1. Title: Atomic Habits | Author: James Clear | ISBN: 9780735211292 | Status: Available
```

After borrowing:

```text
1. Title: Atomic Habits | Author: James Clear | ISBN: 9780735211292 | Status: Borrowed
```

## Example Member Output

```text
1. Name: John Smith | Member ID: M001 | Borrowed Books: 2
```

## Example Borrowed Books Output

```text
Books borrowed by John Smith:

1. Atomic Habits | ISBN: 9780735211292 | Borrowed for: 4 days
2. 1984 | ISBN: 9780451524935 | Borrowed for: 17 days
```

## Late Fine Rules

The late-return system uses the following rules:

```python
MAX_DAYS = 14
FINE_PER_DAY = 0.50
```

The fine is calculated as:

```text
overdue days × fine per day
```

Example:

```text
Book borrowed for: 19 days
Allowed period: 14 days
Overdue: 5 days
Fine: €2.50
```

## What I Learned

This project helped me practice:

- Classes and objects
- Instance methods
- Class methods
- Magic methods such as `__str__`
- Object relationships
- Lists of custom objects
- Separation of responsibilities
- Code organization with modules
- JSON serialization and deserialization
- Converting `datetime` objects to strings
- Restoring strings back to `datetime` objects
- Date calculations
- Business-rule implementation
- Type hints
- File handling
- Search and filtering
- Input validation
- Error handling
- Persistent application state

## Future Improvements

- Replace JSON storage with SQLite
- Add book categories
- Add borrowing history
- Add administrator authentication
- Add automated tests with `pytest`
- Add logging
- Create a graphical interface

## License

This project is open source and available under the MIT License.