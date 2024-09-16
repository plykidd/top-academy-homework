# # Задание 1
# # Дано два текстовых файла. Выяснить, совпадают ли
# # их строки. Если нет, то вывести несовпадающую строку
# # из каждого файла.
# with open("file1.txt", "r", encoding='utf-8') as file1, open("file2.txt", "r", encoding='utf-8') as file2:
#     for l1 in file1:
#         try:
#             l2 = file2.readline()
#         except IndexError:
#             rest = file1.readlines()
#             if rest:
#                 print("<<<\n", *rest, "---\n>>>", sep = '')
#             break
#         if l1 != l2:
#             print("<<<", l1.rstrip(), "---", l2.rstrip(), ">>>", sep = '\n')
#     rest = file2.readlines()
#     if rest:
#         print("<<<\n---\n", *rest, ">>>", sep = '')


# Задание 3
# # Дан текстовый файл. Удалить из него последнюю
# # строку. Результат записать в другой файл
# fr = open('file1.txt', encoding='utf-8')
# fw = open('file2.txt', 'w', encoding='utf-8')
#
# frl = fr.readlines()
# frl = frl[:-1]
#
# for line in frl:
#     fw.write(line)
#
# fr.close()
# fw.close()

# # Задание 4
# # Дан текстовый файл. Найти длину самой длинной
# # строки
# with open("file1.txt") as file:
#     print(max(len(line.strip()) for line in file))

# # Задание 5
# # Дан текстовый файл. Посчитать сколько раз в нем
# # встречается заданное пользователем слово
# import re
# words = re.findall(r'(?i)\bпошел\b', open('file1.txt', 'r', encoding='utf-8').read())
# print(len(words))