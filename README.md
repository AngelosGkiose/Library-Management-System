# Library Management System

A command-line Library Management System built with Python, SQLite, and Object-Oriented Programming.

The application manages books, members, borrowing, returns, book availability, borrowing dates, and late-return fines. All data is stored locally in an SQLite database.

## Features

### Books

* View all books
* Add new books
* Remove available books
* Search books by ISBN
* Track book availability
* Prevent duplicate ISBNs
* Allow books with the same title
* Prevent borrowed books from being removed

### Members

* View all members
* Add new members
* Remove members
* Search members by email
* Validate email addresses
* Prevent duplicate emails
* Prevent members with borrowed books from being removed
* View books borrowed by a specific member

### Borrowing

* Borrow available books
* Return borrowed books
* Store the borrowing date
* Prevent a book from having multiple active loans
* Prevent members from returning books they did not borrow
* Cancel book or member selection by entering `0`

### Late Fines

Books can be borrowed for up to 14 days without a fine.

```python
MAX_DAYS = 14
FINE_PER_DAY = 0.50
```

The fine is calculated using:

```text
overdue days × €0.50
```

Example:

```text
Book 1984 returned successfully by John Smith!
Late return: 5 days overdue. Fine: €2.50
```

## Database

The project uses SQLite and automatically creates a local database named:

```text
book.db
```

The database contains three tables:

* `book`
* `member`
* `loans`

Foreign keys are enabled, and database transactions use `commit` and `rollback` to keep the data consistent.

## Object-Oriented Design

The project contains five main classes:

* `Book` — stores book information and availability
* `Member` — stores member information
* `Loan` — connects books with members and stores borrowing dates
* `Database` — handles SQLite tables, queries, and transactions
* `Library` — handles validation and application rules

## Project Structure

```text
Library-Management-System/
│
├── main.py
├── library.py
├── database.py
├── book.py
├── member.py
├── loan.py
├── README.md
└── .gitignore
```

## Technologies Used

* Python 3
* SQLite
* SQL
* Object-Oriented Programming
* Database transactions
* Foreign keys
* Parameterized queries
* Input validation
* Exception handling
* Date calculations

No external packages are required.

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

On Windows, you can also use:

```bash
py main.py
```

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



## What I Learned

This project helped me practice:

* Classes and objects
* Code organization with modules
* SQLite databases
* SQL queries and joins
* Primary and foreign keys
* Database transactions
* Mapping database rows to Python objects
* Input validation
* Error handling
* Date calculations
* Business rules

## Future Improvements

* Add book categories
* Store complete loan history
* Add due dates
* Add borrowing limits
* Add update functionality
* Add automated tests
* Create a graphical or web interface


