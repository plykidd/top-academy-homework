# Пользователь вводит с клавиатуры три цифры.
# Необходимо создать число, содержащее эти цифры. Например,
# если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157.


numbers1 = str(input("Enter a number: "))
numbers2 = str(input("Enter another number: "))
numbers3 = str(input("Enter a third number: "))

print(numbers1+numbers2+numbers3)

# Задание 2
# Пользователь вводит с клавиатуры число, состоящее
# из четырех цифр. Требуется найти произведение цифр.
# Например, если с клавиатуры введено 1324, тогда результат произведения
# 1*3*2*4 = 24.

numbers = str(input("Enter a number: "))
counter = 1
for number in numbers:
    counter *= int(number)
print(counter)


# Задание 3
# Пользователь вводит с клавиатуры количество метров.
# Требуется вывести реузльтат перевода метров в сантимтры,
# дециметры, миллиметры, мили

numbers = int(input("Enter a number: "))
print('Сантиметры ', numbers*100)
print('Миллиметры ', numbers*1000)
print('Мили',numbers/1610)

# Задание 4
# Напишите программу, вычисляющую площадь треугольника. Пользователь с клавиатуры вводит размер
# основания треугольника и размер высоты

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(
(a+b)/2)

# Задание 5
# Пользователь с клавиатуры вводит четырёхзначное
# число. Необходимо перевернуть число и отобразить
# результат. Например, если введено 4512, результат 2154.

a = int(input("Enter a number: "))
b = str(a)
reversed_number = b[::-1]
new_number = int(reversed_number)

print(new_number)
