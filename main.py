
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.author} - {self.year}"

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.username = None
        self._password = None
        self._email = None

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return True
        else:
            return False
