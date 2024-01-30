__all__ = ['gen_files', 'num_files', 'write_file', 'set_name', 'read_or_begin', 'sum_files']



from random import randint, uniform, choice
from pathlib import Path
from string import ascii_lowercase
from typing import TextIO

MIN_NUN = -1000
MAX_NUM = 1000

def write_file(num: int, name: str | Path) -> None:
    with open(name, 'w', encoding='utf-8') as n:
        for _ in range(num):
            n.write(f'{randint(MIN_NUN, MAX_NUM)} | {uniform(MIN_NUN, MAX_NUM)}\n')

if __name__ == '__main__':
    write_file(10, Path('numbers.txt'))


MIN_VAL = 4
MAX_VAL = 7
VOWELS = 'eyuioa'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def set_name(str_counts: int, file_name: str | Path) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(str_counts):
            name = ''
            flag = choice([-1, 1])
            for _ in range(randint(MIN_VAL, MAX_VAL)):
                if flag == -1:
                    name += choice(CONSONANTS)
                else:
                    name += choice(VOWELS)
                flag *= -1
            f.write(name.title() + '\n')

if __name__ == '__main__':
    set_name(10, Path('names.txt'))

def read_or_begin(fd: TextIO) -> str:
    #print(fd)
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.strip()
def sum_files(f1_name, f2_name, res_file):
    with open(f1_name, 'r', encoding='utf-8') as f1, \
        open(f2_name, 'r', encoding='utf-8') as f2, \
        open(res_file, 'a', encoding='utf-8') as f_res:
        len_f1 = sum(1 for _ in f1)
        len_f2 = sum(1 for _ in f2)
        for _ in range(max(len_f1, len_f2)):
            name = read_or_begin(f1)
            num_int, num_f1 = read_or_begin(f2).split(' | ')
            mult = int(num_int) * float(num_f1)
            f_res.write(f'{name.lower()} {-mult}\n') if mult < 0 \
            else f_res.write(f'{name.upper()} {int(mult)}\n') if mult > 0 else 42


if __name__ == '__main__':
    sum_files(Path('names.txt'), Path('numbers.txt'), Path('results.txt'))

from random import choices, randint, randbytes
from string import ascii_lowercase, digits


# def gen_files(ext: str, min_name: int=6, max_name:int=30, min_size: int=256,
#               max_size: int=256, count: int=1) -> None:
#     for _ in range(count):
#         name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
#         print(name)
#         data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
#         with open(f'{name}.{ext}', 'wb') as f:
#             f.write(data)
#
#
# if __name__ == '__main__':
#     gen_files('bin', count=3)


def gen_files(ext: str, min_name: int=6, max_name:int=30, min_size: int=256,
              max_size: int=256, count: int=1) -> None:
    for _ in range(count):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        print(name)
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)

def num_files(**kwargs) -> None:
    #print(kwargs)
    for ext, count in kwargs.items():
        gen_files(ext, count=count)



if __name__ == '__main__':
    #gen_files('bin', count=3)
    num_files(bin=2, jpeg=1)