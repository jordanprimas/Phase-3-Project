# lib/helpers.py
from models.book import Book
from models.library import Library

def list_libraries():
    library_info = []
    libraries = Library.get_all()
    for i, library in enumerate(libraries, start=1):
        library_info.append((i, library.name, library.id)) 
        print(i, library.name)
    return library_info

def library_details(name):
    library = Library.find_by_name(name)
    if library:
        print(f'Name: {library.name}, Zip code: {library.zip_code}') 
    else:
        print(f"Library {name} not found")

def create_library():
    name = input("Enter the library's name: ")
    zip_code_input = input("Enter the library's zip code: ")

    if zip_code_input.isdigit():
        try: 
            zip_code = int(zip_code_input)
            library = Library.create(name, zip_code)
            print(f'Success: {library.name} created')
        except Exception as exc:
            print("Error creating library: ", exc)
    else:
        print(
            "Error creating library: Zip code must be an integer"
        )

def update_library(id_):
    if library := Library.find_by_id(id_):
        try:
            name = input("Enter the library's new name: ")
            library.name = name
            zip_code = input("Enter the library's new zip code: ")

            if zip_code.isdigit():
                zip_code = int(zip_code)
                library.zip_code = zip_code
                library.update()
                print(f'Success: {library.name} updated')
            else:
                print("Error updating: Zip code must be a number.")
        except Exception as exc:
            print("Error updating library: ", exc)
    else:
        print(f'Error updating: Library not found')


def delete_library(id_):
    if library := Library.find_by_id(id_):
        library.delete()
        print(f'Success: Library deleted')
    else:
        print(f'Error: Library not found')

def list_library_books(library_id):
    book_info = []
    if library := Library.find_by_id(library_id):
        books = library.books()
        for i, book in enumerate(books, start=1):
            book_info.append((i, book.title, book.id))
            print(i, book.title)
    return book_info

def book_details(title):
    book = Book.find_by_title(title)
    if book:
        print(f'Name: {book.title}, Author: {book.author}, Year:{book.year}')

def create_book(id_):
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    year_input = input("Enter the book's publishing year: ")
    library_id = id_

    if year_input.isdigit():
        try:
            year = int(year_input)
            book = Book.create(title, author, year, library_id)
            print(f'Success: Book created')
        except Exception as exc:
            print("Error creating book:", exc)
    else:
        print("Error creating book: year and library id must be numbers")

def update_book(book_id, library_id):
    if book := Book.find_by_id(book_id):
        try:
            title = input("Enter the book's new name: ")
            if title:
                book.title = title
            
            author = input("Enter the book's new author: ")
            if author:
                book.author = author

            year = input("Enter the book's new publishing year: ")
            if year.isdigit():
                book.year = int(year)
            else: 
                print("Error updating: Year must be a number")

            library = library_id 

            book.update()
            print(f'Success: {book.title} updated')
        except Exception as exc:
            print("Error updating book: ", exc)

def delete_book(id_):
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'Success: Book deleted')
    else:
        print(f'Error: Book not found')

def exit_program():
    print("Goodbye!")
    exit()

