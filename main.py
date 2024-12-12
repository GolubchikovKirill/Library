
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
        print(f"Книга {self.title} добавлена в список, всего {self.copies} экземпляров книги")
        return self.copies

    def remove_copies(self, copies):
        """Удаляем копию книги из библиотеки"""
        if self.copies >= 0:
            self.copies -= copies
        else:
            raise ValueError("Экземпляров данной книги 0")
        print(f"Книга {self.title} взята, всего экземпляров книги - {self.copies}")
        return self.copies

class User:
    def __init__(self, first_name, last_name):
        """Класс USER будет описывать человека, который пользуется услугами библиотеки"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = None # По умолчанию None
        self._password = None # По умолчанию None
        self._email = None # По умолчанию None
        self.borrowed_books = [] # Список взятых книг пользователем

    def borrow_book(self, book):
        """Метод для взятия книги человеком."""
        self.borrowed_books.append(book)
        print(f"Книга {book} взята!")
        return book

    def return_book(self, book):
        """Возврат книги человеком"""
        self.borrowed_books.remove(book)
        print(f"Книга {book} возвращена в библиотеку!")
        return book

    def user_book(self, book):
        books = ", ".join([str(book) for book in self.borrowed_books])
        return f"Пользователь {self.first_name} {self.last_name} взял книги: {books}"

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

    def lend_book(self, book, user):
        if book.copies > 0:
            book.remove_copies(1)
            user.borrow_book(book)
            print(f"Книга {self.title} выдана пользователю {user.first_name} {user.last_name}.")
        else:
            print(f"Книга {book.title} недоступна для выдачи!")






