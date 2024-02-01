# lib/helpers.py
from models.book import Book
from models.library import Library

def list_books():
    books = Book.get_all()
    for book in books:
        print(books)

def find_book_by_title():
    title = input("Enter the book's title: ")
    book = Book.find_by_title(title)
    print(book) if title else print(
        f'Book {title} not found'
    )

def find_book_by_id():
    id = input("Enter the book's id: ")
    book = Book.find_by_id(id)
    print(book) if id else print(
        f'Book {id} not found'
    )

def create_book():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    year_input = input("Enter the book's publishing year: ")
    library_id_input = input("Enter the book's library_id: ")
    if year_input is str or library_id_input is str:
        raise ValueError(
            "Error creating book: Input must be an integer."
        )
    else: 
        try:
            year = int(year_input)
            library_id = int(library_id_input)
            book = Book.create(title, author, year, library_id)
            print(f'Success: {book.title} created')
        except Exception as exc:
            print("Error creating book:", exc)

def update_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
            try:
                title = input("Enter the book's new name: ")
                book.title = title 
                author = input("Enter the book's new author: ")
                book.author = author
                year = int(input("Enter the book's new publishing year: "))
                book.year = year
                library_id = int(input("Enter the book's new library_id: "))
                book.library_id = library_id

                book.update()
                print(f'Success: {book.title} updated')
            except Exception as exc:
                print("Error updating book: ", exc)
    else:
        print(f'Book {id_} not found')

def delete_book():
    id_ = int(input("Enter the book's id: "))
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'Book {id_} deleted')
    else:
        print(f'Book {id_} not found')

def find_book_library():
    id_ = int(input("Enter the book's id: "))
    if book := Book.find_by_id(id_):
        library = book.library()
        print(library) if library else print(
            f'Book {id_} not found'
        ) 

def list_libraries():
    libraries = Library.get_all()
    for library in libraries:
        print(library)

def find_library_by_name():
    name = input("Enter the library's name: ")
    library = Library.find_by_name(name)
    print(library) if library else print(
        f"Library {name} not found"
    )

def find_library_by_id():
    id_ = input("Enter the library's id: ")
    library = Library.find_by_id(id_)
    print(library) if library else print(f'Library {id_} not found')

def create_library():
    name = input("Enter the library's name: ")
    zip_code_input = input("Enter the library's zip code: ")

    if zip_code_input is not str:
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

def update_library():
    id_ = input("Enter the library's id: ")
    if library := Library.find_by_id(id_):
        try:
            name = input("Enter the library's new name: ")
            library.name = name
            zip_code = int(input("Enter the library's new zip code: "))
            library.zip_code = zip_code

            library.update()
            print(f'Success: {library.name} updated')
        except Exception as exc:
            print("Error updating library: ", exc)
        else:
            print(f'Library {id_} not found')

def delete_library():
    id_ = input("Enter the library's id: ")
    if library := Library.find_by_id(id_):
        library.delete()
        print(f'Library {id_} deleted')
    else:
        print(f'Library {id_} not found')

def list_library_books():
    id_ = input("Enter library's id: ")
    if library := Library.find_by_id(id_):
        books = library.books()
        for book in books:
            print(book) 
    else: 
        print(f'Library {id_} not found')

def exit_program():
    print("Goodbye!")
    exit()
