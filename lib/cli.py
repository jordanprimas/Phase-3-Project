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


def main():
    while True:
        print("Please select an option:")
        print("Type exit to exit program")
        print("Type L or l to see all libraries")

        choice = input("> ")
        if choice == "exit":
            exit_program()
        elif choice == "L" or choice == "l":
            library_info = list_libraries()
            libraries_menu(library_info)
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
                library_details((library_info[choice - 1][1]))
                library_menu((library_info[choice - 1][2]), library_info)
                
            else:
                print("Invalid choice")
        elif choice == "B" or choice == "b":
            main()
        elif choice == "add":
            create_library()
            list_libraries()
        elif choice == "exit":
            exit_program()
        else:
            print("Invalid choice")

def library_menu(id_, library_info):
    while True:
        print("Type books to see all of the library's books")
        print("Type delete to delete a library")
        print("Type update to update a library")
        print("Type B or b to go back to the previous menu")
        print("Type exit to exit program")

        choice = input("> ")
        if choice == "books":
            books_info = list_library_books(id_) 
            books_menu(id, books_info)  
        elif choice == "delete":
            delete_library(id)
            libraries_menu(library_info)
        elif choice == "update":
            update_library(id)
            libraries_menu(library_info)
        elif choice == "B" or choice == "b":
            libraries_menu(library_info)
        elif choice == "exit":
            exit_program()
        else:
            print("Invalid entry")
        
def books_menu(id_, books_info):
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
                book_title = books_info[choice - 1][1]
                book_num = books_info[choice - 1][0]  

                book_details(book_title)
                book_menu(book_num, books_info)
            else:
                print("Invalid entry")

        elif choice == "add":
            create_book()
        elif choice.lower() == "b":
            library_menu(id_, books_info)
        elif choice.lower() == "exit":
            exit_program()
        else:
            print("Invalid entry")


    
def book_menu(id_, book_info):
     while True:
        print("Type delete to delete this book")
        print("Type update to update this book")
        print("Type B or b to go back to the previous menu")
        print("Type exit to exit program")

        choice = input("> ")
        if choice == "delete":
            delete_book(id_)
        elif choice == "update":
            update_book(id_)
        elif choice == "b" or choice == "B":
            books_menu(id_, book_info)
        elif choice == "exit":
            exit_program()
        else:
            print("Invalid entry")
  

if __name__ == "__main__":
    main()
