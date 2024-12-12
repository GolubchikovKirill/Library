from main import Book, User, Library

book = Book("1984", "Джордж Оруэлл", 1949, 100, 1)
book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1966, 99, 1)
book2 = Book("Убить пересмешника", "Харпер Ли", 1960, 98, 1)

user = User("Kirill","Golubchikov")

print(user.borrow_book(book))
