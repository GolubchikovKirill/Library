
class Book:
    def __init__(self, title, author, year, id, copies):
        """ Создаем 'книгу' с информацией об: title, author, year, ID, copies."""
        self.title = title
        self.author = author
        self.year = year
        self.id = id
        self.copies = copies

    def __str__(self):
        """Текстовое представление книги"""
        return f"{self.title} - {self.author} - {self.year}"

    def add_copies(self, copies):
        """Добавляем копию книги в библиотеку"""
        self.copies += copies
        return self.copies

    def remove_copies(self, copies):
        """Удаляем копию книги из библиотеки"""
        self.copies -= copies
        return self.copies

class User:
    def __init__(self, first_name, last_name):
        """Класс USER будет описывать человека, который пользуется услугами библиотеки"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = None # По умолчанию нет
        self._password = None # По умолчанию нет
        self._email = None # По умолчанию нет
        self.borrowed_books = [] # Список взятых книг пользователем

    def borrow_book(self, book):
        """Метод для взятия книги человеком."""
        self.borrowed_books.append(book)
        return book

    def return_book(self, book):
        """Возврат книги человеком"""
        self.borrowed_books.remove(book)
        return book

class Library:
    """Класс библиотека с списком юзеров и книг"""
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        """Метод добавления книги в список библиотеки"""
        if book not in self.books:
            self.books.append(book)
            return True
        else:
            return False
