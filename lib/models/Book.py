import ipdb

class Book:

    all = []

    def __init__(self, title, author, year, owner=None):
        self.title = title
        self.author = author 
        self.year = year

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

ipdb.set_trace()

          