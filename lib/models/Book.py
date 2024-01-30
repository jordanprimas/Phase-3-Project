# lib/models/book.py
import ipdb
from models.library import Library 
from models.__init__ import CURSOR, CONN

class Book:

    all = []

    def __init__(self, title, author, year, id=None):
        self.id = id
        self.title = title
        self.author = author 
        self.year = year
        self._library = library

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "Title must be a string with at least 1 character."
            )

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, str) and len(author):
            self._author = author
        else:
            raise ValueError(
                "Author must be a string with at least 1 character."
            )

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self._year = year
        else:
            raise ValueError (
                "Year must be an integer."
            )

    @property
    def library(self):
        return self._library

    @library.setter
    def library(self, library):
        if not isinstance(library, Library):
            raise TypeError("Library must be an instance of Library class.")
        self._library = library
    

    #Add create_table" class method to create books table

ipdb.set_trace()

          