# Phase 3 CLI+ORM Project Template

## Introduction
A database for managing books and their libraries.

## Requirements For Generating Your Environment

* Have python installed 

## Repo URL 
[Repository link](https://github.com/jordanprimas/python-p3-conditional-statements.git)

## Interacting With The CLI
`cli.py` is a simple CLI that interacts with a library management database. 
When the user runs the script a menu of options will appear in the terminal. The first loop the user will enter is `main` which gives the option to see all libraries in the database or exit the program. If the user indicates that they want to see libraries then they will be taken to the next loop `libraries_menu`, which will prompt the user to enter the number of a library to see more details. Otherwise they can add a new library and then see the list of all libraries, go back to the previous menu, or exit the program. If the user selects the number of a library they will enter the next loop `library_menu` and this will allow the user to either see all the books in the selected library, delete the library, update the library, go back to the previous menu, or exit the program. Choosing to see all the books will enter the next loop `books_menu` which will prompt the user to enter the number of a book to see more details. There is also the other option of adding a new book, going back to the previous menu, and exiting the program. Choosing a book number will take the user to the final loop `book_menu`. The user will be able to delete or update the book and then either exit the program or return to the previous menu.  

### Interacting With The Models
This project contains two classes with a two way one-to-many relationship model. 

The `book.py` file contains the `Book` class which is responsible for all books within the database. `Book` is initialized with `title`, `author`, `year`, and `library_id`attributes. The `__repr__()` magic method then takes an object and returns a readble string representation. The `title()`,`author()`, and `year()` properties then ensure the validity of the attributes values and raise an error if they are not. The `library_id()` property will also check for the validity of its attribute ensuring that the `library_id` matches the id of a library within the database. The `create_table()` classmethod is used to create a new book table in the database if it doesn't already exist. This table will have all of the previously defined attributes as columns. The `drop_table()` classmethod is used to delete the book table from the database. `save()` will allow the user to save the attributes of a new instance to a book table row with a unique id. `create()` is a classmethod that allows the user create a new book instance and save it to the database in one step. `update()` and `delete()` methods update and delete a book from the database respectivly using its id. `instance_from_db()` retrieves the newest instance from the class variable `all` or if the instance isn't found it updates `all` to contain the newest instance and then returns it. The `get_all()` classmethod queries the database and returns all the books then passes each one to `instance_from_db()` to be formatted. Next the `find_by_title` and `find_by_id` classmethods query the database and return one book matching the input title or id respectivly. Finally `library()` queries the database and returns library with a matching `id` to the instance's `library_id`. 

The `library.py` file contains the `Library` class which is responsible for all libraries within the database. `Library` is initialized with `name` and `zip_code` attributes. The `__repr__()` magic method then takes an object and returns a readble string representation. The `name()` and `zip_code()` properties then ensure the validity of the attributes values and raise an error if they are not. The `create_table()` classmethod is used to create a new library table in the database if it doesn't already exist. This table will have all of the previously defined attributes as columns. The `drop_table()` classmethod is used to delete the library table from the database. `save()` will allow the user to save the attributes of a new instance to a library table row with a unique id. `create()` is a classmethod that allows the user create a new library instance and save it to the database in one step. `update()` and `delete()` methods update and delete a library from the database respectivly using its `id`. `instance_from_db()` retrieves the newest instance from the class variable `all` or if the instance isn't found it updates `all` to contain the newest instance and then returns it. The `get_all()` classmethod queries the database and returns all the libraries then passes each one to `instance_from_db()` to be formatted. Next the `find_by_title` and `find_by_id` classmethods query the database and return one library matching the input title or `id `respectivly. Finally `books()` queries the database and returns all the books with a matching `library_id` to the instance's `id`. 


## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
# Phase-3-Project
