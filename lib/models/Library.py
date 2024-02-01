from models.__init__ import CURSOR, CONN 

class Library:
    all = {}

    def __init__(self, name, zip_code, id=None):
        self.id = id 
        self.name = name 
        self.zip_code = zip_code

    def __repr__(self):
        return (
            f"<Library {self.id}: {self.name}, {self.zip_code}>" 
        )

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name 
        else:
            raise ValueError(
                "Name must be a string with at least 1 character."
            )

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        zip_code_string = str(zip_code)
        if isinstance(zip_code, int) and len(zip_code_string) == 5:
            self._zip_code = zip_code
        else:
            raise ValueError(
                "Zip code must be an integer with 5 characters."
            )

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS libraries (
            id INTEGER PRIMARY KEY,
            name TEXT,
            zip_code INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS libraries
        """
        CURSOR.execute(sql)
        CONN.commit() 

    def save(self):
        sql = """
            INSERT INTO libraries (name, zip_code)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.zip_code))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, zip_code):
        library = cls(name, zip_code)
        library.save()
        return library

    def update(self):
        sql = """
            UPDATE libraries
            SET name = ?, zip_code = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.zip_code, self.id))
        CONN.commit() 
    
    def delete(self):
        sql = """
            DELETE FROM libraries
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        library = cls.all.get(row[0])
        if library:
            library.name = row[1]
            library.zip_code = row[2]
        else:
            library = cls(row[1], row[2])
            library.id = row[0]
            cls.all[library.id] = library
        return library
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM libraries
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM libraries 
            WHERE name = ?
            LIMIt 1
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        if not row:
            return None 
        return cls.instance_from_db(row) 

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * 
            FROM libraries
            WHERE id = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (id,)).fetchone()

        if not row:
            return None 
        return cls.instance_from_db(row)
    
    def books(self):
        from models.book import Book
        sql = """
            SELECT * FROM books
            WHERE library_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        
        return [Book.instance_from_db(row) for row in rows]
    