import sqlite3

from book import Book
from loan import Loan
from member import Member


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('book.db')
        self.cursor = self.connection.cursor()
        self.connection.execute("PRAGMA foreign_keys = ON")

        self.create_table_member()
        self.create_table_book()
        self.create_table_loans()

    def create_table_book(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS book ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT UNIQUE NOT NULL,
        available INTEGER NOT NULL DEFAULT 1)''')
        self.connection.commit()

    def create_table_member(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS member (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)''')
        self.connection.commit()

    def create_table_loans(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS loans (id INTEGER PRIMARY KEY AUTOINCREMENT,book_id Integer  NOT NULL UNIQUE,
        member_id Integer Not Null,borrow_date TEXT NOT NULL,FOREIGN KEY (book_id) REFERENCES book(id),
        FOREIGN KEY (member_id) REFERENCES member(id))""")
        self.connection.commit()


    def get_book_by_title(self, title):
        self.cursor.execute('''SELECT * FROM book WHERE title = ?''', (title,))
        book = self.cursor.fetchone()
        if book is None:
            return None
        else:
            return Book(book[1], book[2], book[3], book[4], book[0])

    def get_book_by_isbn(self, isbn):
        self.cursor.execute('''SELECT * FROM book WHERE isbn = ?''', (isbn,))
        book = self.cursor.fetchone()
        if book is None:
            return None
        else:
            return Book(book[1], book[2], book[3], book[4], book[0])

    def add_book(self, book):
        try:
            self.cursor.execute("Insert into book (title,author,isbn) values(?,?,?)",(book.title,book.author,book.isbn))
            book.book_id = self.cursor.lastrowid
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            self.connection.rollback()
            return False

    def get_member_by_email(self, email):
        self.cursor.execute('''SELECT * FROM member WHERE email = ?''', (email,))
        member = self.cursor.fetchone()
        if member is None:
            return None
        else:
            return Member(member[1], member[2], member[0])


    def add_member(self, member):
        try:
            self.cursor.execute("INSERT INTO member(name,email) VALUES(?,?)",(member.name,member.email))
            member.member_id = self.cursor.lastrowid
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            self.connection.rollback()
            return False

    def get_all_books(self):
        self.cursor.execute('''SELECT * FROM book''')
        rows = self.cursor.fetchall()
        books = []
        for row in rows:
            books.append(Book(row[1], row[2], row[3], row[4], row[0]))
        return books


    def get_all_members(self):
        self.cursor.execute('''SELECT * FROM member''')
        rows = self.cursor.fetchall()
        members = []
        for row in rows:
            members.append(Member(row[1], row[2], row[0]))
        return members

    def borrow_book(self, loan):
        try:
            self.cursor.execute("""
                INSERT INTO loans (
                    book_id,
                    member_id,
                    borrow_date
                )
                VALUES (?, ?, ?)
            """, (
                loan.book_id,
                loan.member_id,
                loan.borrow_date
            ))
            loan.loan_id = self.cursor.lastrowid
            self.cursor.execute("""
                UPDATE book
                SET available = 0
                WHERE id = ?
                  AND available = 1
            """, (loan.book_id,))
            if self.cursor.rowcount != 1:
                self.connection.rollback()
                return False
            self.connection.commit()
            return True
        except sqlite3.Error as error:
            self.connection.rollback()
            print(f"Database error: {error}")
            return False

    def has_borrowed(self,member,book):
        self.cursor.execute("""Select * from loans where book_id=? and member_id=?""",(book.book_id,member.member_id))
        row=self.cursor.fetchone()
        if row is None:
            return False
        else:
            return True

    def get_loan(self,member,book):
        self.cursor.execute("""Select * from loans where member_id=? and book_id=?""",(member.member_id,book.book_id))
        row=self.cursor.fetchone()
        if row is None:
            return None
        else:
            return Loan(row[1], row[2], row[3], row[0])

    def return_book(self, loan):
        try:
            self.cursor.execute("""
                DELETE FROM loans
                WHERE id = ?
            """, (loan.loan_id,))
            if self.cursor.rowcount != 1:
                self.connection.rollback()
                return False
            self.cursor.execute("""
                UPDATE book
                SET available = 1
                WHERE id = ?
                  AND available = 0
            """, (loan.book_id,))
            if self.cursor.rowcount != 1:
                self.connection.rollback()
                return False
            self.connection.commit()
            return True
        except sqlite3.Error as error:
            self.connection.rollback()
            print(f"Database error: {error}")
            return False


    def get_member_borrowed_book(self,member):
        self.cursor.execute("""Select book.* from book join loans on book.id=loans.book_id where loans.member_id=?""",(member.member_id,))
        rows=self.cursor.fetchall()
        member_borrowed_books = []
        for row in rows:
            member_borrowed_books.append(Book(row[1], row[2], row[3], row[4], row[0]))
        return member_borrowed_books

    def remove_book(self,book):
        try:
            self.cursor.execute("""Delete from book where id=?""",(book.book_id,))
            if self.cursor.rowcount != 1:
                self.connection.rollback()
                return False
            self.connection.commit()
            return True
        except sqlite3.Error as error:
            self.connection.rollback()
            print(f"Database error: {error}")
            return False

    def has_no_borrowed_books(self,member):
        self.cursor.execute("""Select * from loans where member_id=?""",(member.member_id,))
        rows=self.cursor.fetchall()
        if len(rows)==0:
            return True
        else:
            return False

    def remove_member(self,member):
        try:
            self.cursor.execute("""Delete from member where id=?""", (member.member_id,))
            if self.cursor.rowcount != 1:
                self.connection.rollback()
                return False
            self.connection.commit()
            return True
        except sqlite3.Error as error:
            self.connection.rollback()
            print(f"Database error: {error}")
            return False

    def close(self):
        self.connection.close()