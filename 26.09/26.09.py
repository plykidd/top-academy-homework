# # Создайте класс «Дробь». Необходимо хранить в полях
# # класса: числитель и знаменатель. Реализуйте методы класса
# # для ввода данных, вывода данных, реализуйте доступ к
# # отдельным полям через методы класса. Также создайте
# # методы класса для выполнения арифметических операций
# # (сложение, вычитание, умножение, деление, и т.д.).
# # К уже реализованному классу «Дробь»
# # добавьте статический метод,
# # который при вызове возвращает количество созданных объектов
# # класса «Дробь»
#
# from __future__ import annotations
#
#
# class Fraction:
#     def __init__(self, numerator: int, denominator: int, int_part: int = 0):
#         self.__num: int = numerator + int_part * denominator
#         self.__den: int = denominator
#
#     @property
#     def num(self) -> int:
#         return self.__num
#
#     @num.setter
#     def num(self, value):
#         if type(value) == int:
#             self.__num = value
#
#     def add(self, fraction: Fraction) -> Fraction:
#         num = self.__num * fraction.__den + fraction.__num * self.__den
#         den = self.__den * fraction.__den
#         return Fraction(num, den)
#
#     def multiply(self, fraction: Fraction) -> Fraction:
#         num = self.__num * fraction.__num
#         den = self.__den * fraction.__den
#         return Fraction(num, den)
#
#     def __str__(self) -> str:
#         num = self.__num
#
#         if self.__num > self.__den:
#             int_part = int(self.__num / self.__den)
#             num -= int_part * self.__den
#             return f'{int_part} ({num}/{self.__den})'
#         elif self.__num == self.__den:
#             return str(int(self.__num / self.__den))
#
#         return f'{self.__num}/{self.__den}'
#
#     def __float__(self):
#         return self.__num / self.__den
#
#
# f1: Fraction = Fraction(10, 4)
# f2: Fraction = Fraction(42, 2)
#
# f3: Fraction = f1.add(f2)
# print(f3)
# print(float(f3))


# # Задание 2
# # Создайте класс для конвертирования температуры из
# # Цельсия в Фаренгейт и наоборот. У класса должно быть
# # два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# # класс должен считать количество подсчетов температурыи
# # возвращать это значение с помощью статического метода.
#
#
# class Converter:
#     count = 0
#
#     @staticmethod
#     def celsius_of_fahrenheit(celsius):
#         Converter.count += 1
#         return (celsius * 9/5) + 32
#
#     @staticmethod
#     def fahrenheit_of_celsius(fahrenheit):
#         Converter.count += 1
#         return (fahrenheit - 32) * 5/9
#
#     @staticmethod
#     def get_count():
#         return Converter.count
#
#
# print(Converter.fahrenheit_of_celsius(10))
# print(Converter.celsius_of_fahrenheit(10))


# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

# class Converter:
#    num: float = 3.28084
#     @staticmethod
#     def meters_to_feet(meters):
#         return meters * Converter.num
#
#     @staticmethod
#     def feet_to_meters(feet):
#         return feet / Converter.num
#
# print(Converter.meters_to_feet(124142))
