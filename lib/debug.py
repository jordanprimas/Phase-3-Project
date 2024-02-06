#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.book import Book
from models.library import Library
import ipdb

def reset_database():
    Book.drop_table()
    Library.drop_table()
    Book.create_table()
    Library.create_table()

    # Seed data
    library_one = Library.create("library_one", 12345)
    library_two = Library.create("library_two", 22034)
    
    Book.create("book_one", "author_one", 2019, library_one.id)
    Book.create("book_two", "author_two", 1311, library_one.id)
    Book.create("book_three", "author_three", 2039, library_two.id)
    Book.create("book_four", "author_four", 1223, library_two.id)
    Book.create("book_five", "author_five", 2345, library_two.id)

reset_database()
ipdb.set_trace()
