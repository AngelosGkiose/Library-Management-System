
from library import Library


def show_menu():
    print("""===== Library Management System =====

1. View All Books
2. View All Members
3. Add Book
4. Add Member
5. Borrow Book
6. Return Book
7. View Member's Borrowed Books
8. Remove Book
9. Remove Member
10. Exit""")


def main():
    library = Library()
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            library.view_books()
        elif choice == "2":
            library.view_members()
        elif choice == "3":
            library.add_book()
        elif choice == "4":
            library.add_member()
        elif choice == "5":
            library.borrow_book()
        elif choice == "6":
            library.return_book()
        elif choice == "7":
            library.view_members_books()
        elif choice == "8":
            library.delete_book()
        elif choice == "9":
            library.remove_member()
        elif choice == "10":
            print("Bye!")
            break
        else:
            print("Please enter a valid choice (1-10)")


if __name__ == '__main__':
    main()