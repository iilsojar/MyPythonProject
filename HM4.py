#Напишите функцию для транспонирования матрицы
#
# from random import randint as r
# def create_matrix(n): #создаем матрицу
#     matrix = []
#     for _ in range(n):
#         matrix.append([r(1,9) for i in range(n)])
#     return matrix
#
# def print_matrix(matrix): #печатаем матрицу
#     for i in matrix:
#         print(i)
#
# def transpond_matrix(matrix):
#     for j in range(len(matrix)):
#         for i in range(len(matrix)):
#             print(matrix[i][j], end=' ')
#         print()
#
# NUMBER = 5
# matrix = create_matrix(NUMBER)
# print('Матрица:')
# print_matrix(matrix)
# print('Транспонированная матрица:')
# print(transpond_matrix(matrix))


#Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление

'''Возвращает словарь, где ключ — значение переданного в функцию аргумента, а значение — имя аргумента'''
# def my_dict(**kvargs):
#     new_dict = {}
#     for values, key in kvargs.items():
#         new_dict[str(key)] = values
#     return new_dict
#
# print(my_dict(first=1, second='два', third=True, four = 3.14))

#Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import time

def refill_withdraw(balance, count, mode, commission):

    global history_operations

    money_commission = 0 + commission

    while True:
        money = int(input('Введите сумму пополнения (кратную 50): '))
        if money % 50 == 0:
            break
        else:
            print('Повторите попытку')

    if count == 3:
        money_commission += 0.03

    match mode:
        case 1:
            money_value = (money - (money * money_commission))
            balance += money_value
            history_operations.append(f'Пополнение +{money_value}')
        case 2:
            if money > balance:
                print('Ошибочная операция!')
                return balance
            if money * (0.015 + money_commission) <= 30:
                money_value = (money + 30)
                balance -= money_value
                history_operations.append(f'Снятие средств -{money_value}')
            elif money * (0.015 + money_commission) >= 600:
                money_value = (money + 600)
                balance -= money_value
                history_operations.append(f'Снятие средств -{money_value}')
            else:
                money_value = (money + (money * (0.015 + money_commission)))
                balance -= money_value
                history_operations.append(f'Снятие средств -{money_value}')

    return balance


def print_history_operation():

    global history_operations

    print('\n')
    for number, value in enumerate(history_operations, 1):
        print(f'{number}. {value}')


balance = 0
number_operations = 0
money_commission = 0
history_operations = []

while True:
    print(f'\nВведите номер операции:\n'
      '1. Пополнение счета\n'
      '2. Снятие наличных\n'
      '3. Показать баланс\n'
      '4. История операций\n'
      '5. Выйти\n')

    mode = int(input('Введите номер операции: '))

    if balance >= 5_000_000:
        money_commission = 10

    match mode:
        case 1:
            balance = refill_withdraw(balance, number_operations, mode, money_commission)
            number_operations += 1
        case 2:
            if balance != 0:
                balance = refill_withdraw(balance, number_operations, mode, money_commission)
                number_operations += 1
            else:
                print('Нулевой баланс!')
        case 3:
            print(f'\nВаш баланс: {balance}')
            time.sleep(2)
        case 4:
            print_history_operation()
            time.sleep(2)
        case 5:
            break