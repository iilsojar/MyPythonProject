# 2. Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

DIV_HEX = 16

number = int(input('Введите десятичное число: '))
hex_digits = '0123456789abcdef'
hex_number = ''

while number > 0:
    remainder = number % DIV_HEX
    hex_digit = hex_digits[remainder]
    hex_number = hex_digit + hex_number
    number //= DIV_HEX
print("Шестнадцатеричное число:", hex_number)

#Проверка через формулу

number = int(input('Введите десятичное число: '))
hex_number = hex(number)
print(hex_number)

# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions


import fractions

f1 = fractions.Fraction(input('Введите первую дробь: '))
print(f1)
f2 = fractions.Fraction(input('Введите вторую дробь: '))
print(f2)
sum = f1 + f2
mult = f1 * f2
print(f'{f1} + {f2} = {sum}\n{f1} * {f2} = {mult}')