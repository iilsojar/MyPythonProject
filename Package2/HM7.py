# 2. Напишите функцию группового переименования файлов.
# Она должна:
# a. принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os
from pathlib import Path
from random import choices, randint, randbytes
from string import ascii_lowercase, digits

__all__ = ['rename_file']

"""
Переименование файлов. Возвращает количество переименованных файлов.

       :new_name: новое имя файла
       :count: количество цифр в нумераторе
       :ext_old: расширение 
       :ext_new: новое расширение
       :r_range: диапазон букв
       :path: каталог
"""
def rename_file(new_name: str, ext_old: str, count: int=3, ext_new: str = None, r_range: range = (3, 6), path: str = None) -> int:
    if ext_new is None:
        ext_new = ext_old
        work_path = Path.cwd() if path is None else Path(path)
        count = 0
        for p in work_path.iterdir():
            if p.is_file() and p.suffix == ext_old:
                file_name = f"{p.stem[r_range[0]:r_range[1]]}{new_name}{count:03}{ext_new}"
                p.rename(Path(p.parent, file_name))
                count += 1

        return count

if __name__ == '__main__':
    rename_file("nnt", ".txt")

