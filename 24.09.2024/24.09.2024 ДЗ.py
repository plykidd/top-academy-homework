# # # Задание 1
# # # Реализуйте класс «Автомобиль». Необходимо хранить
# # # в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# # # методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# #
# #
#
#
# class Cars:
#     def __init__(self, name, year, director, engine, color, price):
#         self.name = name
#         self.year = year
#         self.director = director
#         self.engine = engine
#         self.color = color
#         self.price = price
#
#     def print(self):
#         print(self.name, self.year, self.director, self.engine, self.color, self.price)
#         print('\n')
#
#     def __str__(self):
#         return self.name
#
#
# car1: Cars = Cars('mers', 2000, 'Germany', 5, 'white', 2000)
# car1.print()

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы
#
# class Book:
#     def __init__(self, name, year, producer, genre, author, price):
#         self.name = name
#         self.year = year
#         self.producer = producer
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def print_book(self):
#         print(f"Your name is {self.name}")
#         print(f"Your year is {self.year}")
#         print(f"Your producer is {self.producer}")
#         print(f"Your genre is {self.genre}")
#         print(f"Your author is {self.author}")
#         print(f"Your price is {self.price}")
#
#     def __str__(self) -> str:
#         return f"Your name is {self.name}"
#
#
# a1: Book = Book("War and World", "1999", "<NAME>", "<NAME>", "1999", 2000)
# a1.print_book()


# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса

# Все тоже самое, просто поменяются название классов и переменных.
