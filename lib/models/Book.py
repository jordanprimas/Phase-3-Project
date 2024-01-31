# lib/models/book.py
import ipdb
from library import Library 
from __init__ import CURSOR, CONN

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
    

    #Add create_table" class method to create books table if doesn't already exist
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books
                (id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER)
        """

        CURSOR.execute(sql)
    
    #Add drop_table method to drop "pets" Table if exists
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books
        """

        CURSOR.execute(sql)
    
    #Add "save" instance method to persist new "pet" instances to DB
    def save(self):
        sql = """
            INSERT INTO books (title, author, year)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.author, self.title))

    #Add "create" Class Method to initialize and save new "book" instances to DB 
    #Persists new "book" instance to DB and creates an object that is an instance of the Department class
    @classmethod
    def create(cls, title, author, year):
        book = cls(title, author, year)
        book.save()
        return book 

    #Add "new_from_db" class method to retrieve the newest book instance with attributes from DB
    @classmethod
    def new_from_db(cls, row):
        book = cls(
           title=row[1],
           author=row[2],
           year=row[3],
           id=row[0]
        )

        return book 


ipdb.set_trace()

          