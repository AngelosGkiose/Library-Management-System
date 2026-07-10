#  Library Management System

A command-line Library Management System built with Python using Object-Oriented Programming (OOP).

The application allows users to manage a library by adding, searching, deleting, borrowing, and returning books while storing data in a JSON file.

---

## Features

-  View all books
-  Add new books
-  Delete books
-  Search books by title or author
-  Borrow books
-  Return borrowed books
-  Persistent storage using JSON
-  Input validation and error handling

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling

---

## Project Structure

```
Library-Management-System/
│
├── library.py
├── books.json
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/library-management-system.git
```

Move into the project folder:

```bash
cd library-management-system
```

Run the application:

```bash
python library.py
```

---

## Menu

```
===== Library Management System =====

1. View Books
2. Add Book
3. Delete Book
4. Search Book
5. Borrow Book
6. Return Book
7. Exit
```

---

## Example

```
1. Title: Atomic Habits
   Author: James Clear
   ISBN: 12345
   Status: Available
```

After borrowing:

```
1. Title: Atomic Habits
   Author: James Clear
   ISBN: 12345
   Status: Borrowed
```

---

## What I Learned

This project helped me practice:

- Object-Oriented Programming (Classes & Objects)
- Class methods and instance methods
- Object serialization with JSON
- Converting objects to dictionaries
- Loading objects from JSON
- File handling
- CRUD operations
- Data validation
- Error handling
- Clean code organization

---

## Future Improvements

- SQLite database support
- Multiple copies of the same book
- Book categories
- Due dates for borrowed books
- User accounts
- Book availability statistics
- Export library data

---

## License

This project is open source and available under the MIT License.
