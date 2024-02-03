# 1) Напишите функцию, которая принимает список, из списка выдает случайное
# значение из списка и записывает результат в txt файл. Список language =
# ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]

# import random

# def random_language(language_list, filename):
#     random_index = random.randint(0, len(language_list) - 1)

#     random_language_from_list = language_list[random_index]

#     with open(filename, 'w') as file:
#         file.write(random_language_from_list)

# language_list = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]

# random_language(language_list, 'random_language.txt')

# 2) У нас есть переменная text которая, хранит в себе текст:
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.
# Откройте файл text.txt и запишите текст в файл 2 способами

# 1 способ

# def first_way(text, filename):
#       with open(filename, 'w') as file:
#             file.write(text)

# text = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.'''

# first_way(text, 'text1.txt')

# 2 способ

# def second_way(text, filename):
#     file = open(filename, 'w')
#     file.write(text)
#     file.close()
# text = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.'''
# second_way(text, 'text2.txt')

# ДОП ЗАДАЧА:
# 3) Написать программу, которая откроет созданный в задаче 2 файл text.txt,
# скопирует весь текст и запишет его в новый файл wikipedia.txt .

# def copy(text, filename, new_filename):
#     with open(filename, 'w') as file:
#         file.write(text)

#     with open(filename, 'r') as file:
#         copy_text = file.read()

#     with open(new_filename, 'w') as file:
#         file.write(copy_text)

# text = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.'''

# copy(text, 'text.txt', 'wikipedia.txt')


# 4) Создайте модуль с двумя функциями, которые вычисляли бы периметр и
# площадь прямоугольника. Подключите этот модуль к основной программе и
# вызовите эти функции с аргументами.

# from периметр import perimeter, area

# width = int(input("Введите ширину прямоугольника:"))
# length = int(input("Введите длину прямоугольнка:"))

# perimeterr = perimeter(width, length)
# arrea = area(width, length)

# print(perimeterr)
# print(arrea)

# 5) У нас есть список list = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]. Написать функцию которая
# переворачивает список. И используйте эту функцию на другом файле

# 1 способ
# def turn_over(filename):
#       with open(filename, 'r') as file:
#             a = file.read()

#       print(a[::-1])
# turn_over('baki.txt')

# 2 способ
# from baki import list

# def turn_overr():
#       print(list[::-1])
# turn_overr()

# 6) Написать функцию, которая принимает hour(час), min(минуту), sec(секунды). И
# вам нужно превратить их в секунды. Вызовите его на другом файле

def time(hour, min, sec):
      sec_hour = hour * 3600
      sec_min = min * 60 

      return sec_hour + sec_min + sec