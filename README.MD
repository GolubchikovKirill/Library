# Описание проекта: “Управление библиотекой”

Цель — создать систему управления библиотекой, которая позволяет:
	1.	Хранить данные о книгах и их экземплярах.
	2.	Учет пользователей (читателей).
	3.	Отслеживать выдачу и возврат книг.
	4.	Добавлять/удалять книги и пользователей.

Основные компоненты и классы
1.	Book
	•	Атрибуты:
	•	title (название книги)
	•	author (автор книги)
	•	isbn (уникальный идентификатор)
	•	copies (количество доступных копий)
	•	Методы:
	•	add_copies(n) — добавляет экземпляры.
	•	remove_copies(n) — убирает экземпляры.
2.	User
	•	Атрибуты:
	•	user_id (уникальный ID)
	•	name (имя пользователя)
	•	borrowed_books (список взятых книг)
	•	Методы:
	•	borrow_book(book: Book) — взять книгу.
	•	return_book(book: Book) — вернуть книгу.
3.	Library
	•	Атрибуты:
	•	books (список всех книг)
	•	users (список пользователей)
	•	Методы:
	•	add_book(book: Book)
	•	remove_book(book: Book)
	•	add_user(user: User)
	•	remove_user(user: User)
	•	lend_book(book: Book, user: User) — выдать книгу.
	•	receive_book(book: Book, user: User) — принять книгу.
Exceptions (дополнительно)
Создай собственные исключения:
	•	BookNotAvailableException — если книга недоступна.
	•	UserNotFoundException — если пользователь не найден.
	•	LimitExceededException — если пользователь превысил лимит взятых книг.

	1.	Реализация классов. Начни с простого: реализуй базовые атрибуты и методы классов Book и User.
	2.	Логика библиотеки. Перейди к классу Library и добавь методы для управления пользователями и книгами.
	3.	Обработка ошибок. Напиши исключения и используй их для контроля ошибок (например, пользователь берет больше книг, чем разрешено).
	4.	Тестирование. Создай тестовые данные и напиши скрипт для проверки функциональности системы.