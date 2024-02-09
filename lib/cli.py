# lib/cli.py

from helpers import (
    list_libraries,
    library_details,
    create_library,
    update_library,
    delete_library,
    list_library_books,
    book_details,
    create_book,
    update_book,
    delete_book,
    exit_program
)

separator = ('*' * 40)

def main():
    while True:
        print("Please select an option:")
        print("Type exit to exit program")
        print("Type L or l to see all libraries")

        choice = input("> ")
        if choice == "L" or choice == "l":
            print(separator)
            library_info = list_libraries()
            print(separator)
            libraries_menu(library_info)
        elif choice == "exit":
            exit_program()
        else:
            print("Invalid choice")  


def libraries_menu(library_info):
    while True: 
        print("Please select the number of a library for more details:")
        print("or")
        print("Type add to add a new library to the database")
        print("Type B or b to go back to the previous menu")
        print("Type exit to exit program")

        choice = input("> ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(library_info):
                library_name = library_info[choice - 1][1]
                library_id = library_info[choice - 1][2]

                print(separator)
                library_details(library_name)
                print(separator)

                library_menu(library_id, library_info)
                
            else:
                print("Invalid choice")
        elif choice == "add":
            create_library()
            print(separator)
            library_info = list_libraries()
            print(separator)

        elif choice == "B" or choice == "b":
            main()
        elif choice == "exit":
            exit_program()
        else:
            print("Invalid choice")

def library_menu(library_id, library_info):
    while True:
        print("Type books to see all of the library's books")
        print("Type delete to delete the library")
        print("Type update to update the ibrary")
        print("Type B or b to go back to the previous menu")
        print("Type exit to exit program")

        choice = input("> ")
        if choice == "books":
            print(separator)
            books_info = list_library_books(library_id) 
            print(separator)
            books_menu(library_id, library_info, books_info)  
        elif choice == "delete":
            delete_library(library_id)
            main()
        elif choice == "update":
            update_library(library_id)
        elif choice == "B" or choice == "b":
            libraries_menu(library_info)
        elif choice == "exit":
            exit_program()
        else:
            print("Invalid entry")
        
def books_menu(library_id, library_info, books_info):
    while True:
        print("Please select the number of a book for more details:")
        print("or")
        print("Type add to add a new book to the database")
        print("Type B or b to go back to the previous menu")
        print("Type exit to exit program")

        choice = input("> ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(books_info):
                book_id = books_info[choice - 1][2]
                book_title = books_info[choice - 1][1]  

                print(separator)
                book_details(book_title)
                print(separator)
                
                book_menu(book_id, books_info, library_id, library_info)
            else:
                print("Invalid entry")

        elif choice == "add":
            create_book(library_id)
            print(separator)
            books_info = list_library_books(library_id) 
            print(separator)

        elif choice.lower() == "b":
            library_menu(library_id, library_info)
        elif choice.lower() == "exit":
            exit_program()
        else:
            print("Invalid entry")


    
def book_menu(book_id, books_info, library_id, library_info):
     while True:
        print("Type delete to delete this book")
        print("Type update to update this book")
        print("Type B or b to go back to the previous menu")
        print("Type exit to exit program")

        choice = input("> ")
        if choice == "delete":
            delete_book(book_id)
            books_menu(library_id, library_info, books_info)
        elif choice == "update":
            update_book(book_id, library_id)
        elif choice == "b" or choice == "B":
            books_menu(library_id, library_info, books_info)
        elif choice == "exit":
            exit_program()
        else:
            print("Invalid entry")
  

if __name__ == "__main__":
    main()
