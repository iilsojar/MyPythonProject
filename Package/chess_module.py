# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# рограмма получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


__all__ = ['solve', 'set']

# x1 = int(input(''))
# y1 = int(input(''))
# x2 = int(input(''))
# y2 = int(input(''))
# if x1 == x2 or y1 == y2:
#     print('YES')
# elif x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
#     print('YES')
# else:
#     print('NO')

board = [[0 for i in range(8)] for j in range(8)]

def set(i, j):
    for x in range(8):
        board[x][j] += 1
        board[i][x] += 1
        if i + j - x >= 0 and i + j - x < 8:
            board[i + j - x][x] += 1
        if i - j + x >= 0 and i - j + x < 8:
            board[i - j + x][x] += 1
    board[i][j] = -1

def remove(i, j):
    for x in range(8):
        board[x][j] -= 1
        board[i][x] -= 1
        if i + j - x >= 0 and i + j - x < 8:
            board[i + j - x][x] -= 1
        if i - j + x >= 0 and i - j + x < 8:
            board[i - j + x][x] -= 1
    board[i][j] = 0

def print_place():
    abc = 'abcdegfh'
    ans = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                ans.append(abc[j] + str(i + 1))
    print(', '.join(ans))

def solve(i):
    for j in range(8):
        if board[i][j] == 0:
            set(i, j)
            if i == 7:
                print_place()
            else:
                solve(i + 1)
            remove(i, j)

solve(0)
