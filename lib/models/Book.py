# lib/models/book.py
import ipdb
from library import Library 
from __init__ import CURSOR, CONN

class Book:

    all = {}

    def __init__(self, title, author, year, id=None):
        self.id = id
        self.title = title
        self.author = author 
        self.year = year
        #self._library = library

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
                year INTEGER),
                library_id INTEGER,
                FOREIGN KEY (library_id) REFERENCES library(id))
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    #Add drop_table method to drop "pets" Table if exists
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    #Add "save" instance method to persist new "pet" instances to DB
    def save(self):
        sql = """
            INSERT INTO books (title, author, year, library_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.author, self.year, self.library_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    #Add "create" Class Method to initialize and save new "book" instances to DB 
    #Persists new "book" instance to DB and creates an object that is an instance of the Department class
    @classmethod
    def create(cls, title, author, year, library_id):
        book = cls(title, author, year, library_id)
        book.save()
        return book 

    def update(self):
        sql = """
            UPDATE books
            SET title = ?, author = ?, year = ?, library_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.author, self.year, self.library_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None 

    #Add "new_from_db" class method to retrieve the newest book instance with attributes from DB
    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book: 
           book.title = row[1],
           book.author = row[2],
           book.year = row[3],
           book.library_id=row[4]
        else:
            book = cls(row[1], row[2], row[3], row[4])
            book.id = row[0]
            cls.all[book.id] = book 
        return book 

    #Add "get_all" class method to retrieve all "book" instances from DB
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM books
        """
        return [cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]
    
    #Add "find_by_title" class method to retrieve "book" instance by "title" attribute from DB
    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT * FROM books
            WHERE title = ?
            LIMIT 1
        """

        row = CURSOR.execute(sql, (title,)).fetchone()

        #Return None if no "row" is found 
        if not row:
            return None 
        
        #else instatiate Book class with tuple values and return that instance
        return cls.instance_from_db(row)

    #Add "find_by_id" class method to retrieve book instace by id attribute from DB
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM books
            WHERE id = ?
            LIMIT 1
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if not row:
            return None 

        return cls.instance_from_db(row)

ipdb.set_trace()

          