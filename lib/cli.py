# lib/cli.py

from helpers import (
    exit_program,
    list_books,
    find_book_by_title,
    find_book_by_id,
    create_book,
    update_book,
    delete_book,
    find_book_library,
    list_libraries,
    find_library_by_name,
    find_library_by_id,
    create_library,
    update_library,
    delete_library,
    list_library_books,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_books()
        elif choice == "2":
            find_book_by_title()
        elif choice == "3":
            find_book_by_id()
        elif choice == "4":
            create_book()
        elif choice == "5":
            update_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            find_book_library()
        elif choice == "8":
            list_libraries()
        elif choice == "9":
            find_library_by_name()
        elif choice == "10":
            find_library_by_id()
        elif choice == "11":
            create_library()
        elif choice == "12":
            update_library()
        elif choice == "13":
            delete_library()
        elif choice == "14":
            list_library_books()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all books")
    print("2. Find book by title")
    print("3. Find book by id")
    print("4. Create book")
    print("5. Update book")
    print("6. Delete book")
    print("7. Find library where a book is located")
    print("8. List all libraries")
    print("9. Find library by name")
    print("10. Find library by id")
    print("11. Create library")
    print("12. Update library")
    print("13. Delete library")
    print("14. List all books in a library")


if __name__ == "__main__":
    main()
