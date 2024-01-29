# import random as rnd
# import pandas as pd
# import numpy as np
# import seaborn as sc
#
# from decimal import Decimal as D

from random import randint
from sys import argv

__all__ = ['func']

def func(low:int=0, up:int=100, counter:int=10)->bool:
    num = randint(low, up)
    for _ in range(counter):
        number = int(input('enter the number: '))
        if number < num:
            print('the number is bigger!')
        elif number > num:
            print('the number is smaller!')
        else:
            print('Congrat!!!!')
            return True
    print('Sorry!')
    return False

if __name__ == '__main__':
    func()

def func(low:int=0, up:int=100, counter:int=10)->bool:
    num = randint(low, up)
    for _ in range(counter):
        number = int(input('enter the number: '))
        if number < num:
            print('the number is bigger!')
        elif number > num:
            print('the number is smaller!')
        else:
            print('Congrat!!!!')
            return True
    print('Sorry!')
    return False

if __name__ == '__main__':
    low, up, counter = list(map(int, argv[1:4]))
    func(low, up, counter)