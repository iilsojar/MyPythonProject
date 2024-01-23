#Напишите функцию, которая принимает на вход строку -
# абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.

# import os
#
# print("Введите абсолютный путь до файла: ")
# s = str(input())
# a, b = os.path.split(s)
# b, c = b.split('.')
# result = (a, b, c)
# print(result)

#Напишите однострочный генератор словаря, который принимает на вход
# три списка одинаковой длины: имена str, ставка int, премия str с
# указанием процентов вида “10.25%”. В результате получаем словарь с
# именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# def func(names, salary, bonus):
#     res = {name: salary * float(bonus[:-1]) / 100
#          for name, salary, bonus in zip(names, salary, bonus)}
#     return res
#
# names = ['Иван', 'Николай', 'Петр', 'Харитон']
# salary = [125_000, 96_000, 109_000, 100_000]
# bonus = ['10%', '25.5%', '13.3%', '42.73%']
#
# #print(func(name, salary, bonus))
#
# print({names: (salary * float(bonus[:-1]) / 100) for names, salary, bonus in zip(names, salary, bonus)})

#Создайте функцию генератор чисел Фибоначчи

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# SIZE = 10
#
# fib = iter(fibonacci())
# for _ in range(SIZE):
#     print(next(fib), end=' ')
