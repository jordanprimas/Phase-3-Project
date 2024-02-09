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
    dallas_library = Library.create("Dallas Library", 75912)
    seattle_library = Library.create("Seattle Library", 98127)
    miami_library = Library.create("Miami Library", 33478)

    
    Book.create("The Great Gatsby", "F. Scott Fitzgerald", 1925, dallas_library.id)
    Book.create("Pride and Prejudice", "Jane Austen", 1813, dallas_library.id)
    Book.create("The Hunger Games", "Suzanne Collins", 2008, seattle_library.id)
    Book.create("The Hobbit", "J.R.R. Tolkien", 1937, miami_library.id)
    Book.create("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, miami_library.id)

reset_database()
ipdb.set_trace()
