
#проверить год на високосность

# BIG_LEAP_YEAR = 400
# SMALL_LEAP_YEAR = 4
# LARGE_NOT_BIG_YEAR = 100
# MULTIPLE = 0
# REFORM = 1582
# year = int(input('Введите год в формате yyyy: '))
# if year < REFORM:
#     result = f'{year} год до ввода григорианского календаря, введите другой год'
# elif not year % BIG_LEAP_YEAR:
#     result = f'Год {year} высокосный'
# elif not year % LARGE_NOT_BIG_YEAR:
#     result = f'Год {year} НЕ высокосный'
# elif not year % SMALL_LEAP_YEAR:
#     result = f'Год {year} высокосный'
# else:
#     result = f'Год {year} НЕ высокосный'
# print(result)

LOWER_LIMIT = 1
UPPER_LIMIT = 999
ONE = 1
TEN = 10
HUNDRED = 100

num = LOWER_LIMIT - ONE
while num < LOWER_LIMIT or num > UPPER_LIMIT:
    num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
if num < TEN:
    result = f'число {num} - цифра. Ее квадрат равен {num*num}'
elif num < HUNDRED:
    f_num = num // TEN
    s_num = num % TEN
    result = f'число {num} - двухзначное. Произведение цифр равно {f_num * s_num}'
else:
    f_num = num // HUNDRED
    s_num = num // TEN % TEN
    t_num = num % TEN
    result = f'число {num} - трехзначное. Ее зеркальное отображение равно {t_num * HUNDRED + s_num * TEN + f_num}'
print(result)

# LOWER_LIMIT = 2
# UPPER_LIMIT = 11
# COLUMNS = 4
#
# for row in (LOWER_LIMIT, LOWER_LIMIT+COLUMNS):
#     for num_2 in range(LOWER_LIMIT, UPPER_LIMIT):
#         for num_1 in range(row, row + COLUMNS):
#             print(f'{num_1:>2} x {num_2: >2} = {num_1 * num_2:>2}', end='\t')
#         print()
#     print()

# SPACE = ' '
# STAR = '*'
# ONE = 1
#
# rows = int(input('Введите количество рядов у елки: '))
# spaces = rows - ONE
# stars = ONE
#
# for i in range(rows):
#     print(spaces * SPACE + stars * STAR)
#     spaces -= 1
#     stars += 2


# MIN = 0
# MAX = 100000
#
# num = float(input(f'Введите число от {MIN} до {MAX}: '))
# if num // num == 1 and num // 1 == num:
#     print(f'введенное число {num} - простое')
# else:
#     print(f'введенное число {num} - составное')


