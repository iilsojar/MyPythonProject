"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку
"""

__all__ = ['check_date']

def _leap_year(year:int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

def check_date(date):
    day, month, year = list(map(int, date.split('.')))
    flag = False

    if 1 <= year <= 9999 and 1 <= month < 13 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            flag = True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            flag = True
        else:
            flag = _leap_year(year) and day <= 29

    return f'\n\tПроверка даты - {flag}'

if __name__ == '__main__':
    print(check_date('13.01.1980'))
    print(check_date('01.13.1980'))
    print(check_date('31.2.2021'))
    print(check_date('32.3.2020'))

from sys import argv
from year_module import check_date

print(check_date())