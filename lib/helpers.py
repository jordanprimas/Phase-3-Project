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
    year = int(input("Enter the book's publishing year: "))
    library_id = int(input("Enter the book's library_id: "))
    try:
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
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'Book {id_} deleted')
    else:
        print(f'Book {id_} not found')

def list_all_library_books():
    id_ = input("Enter the library's id: ")

    if library := Library.find_by_id(id_):
        books = library.books()
        for book in books:
            print(book) 
    else: 
        print(f'Book {id_} not found')



def exit_program():
    print("Goodbye!")
    exit()
