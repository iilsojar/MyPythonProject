"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
"""
__all__ = ['save_to_json', 'save_to_csv', 'save_to_picle', 'dir_info', 'dict_info', 'file_info']

import os
from pathlib import Path
import json
import csv
import pickle

MAIN = 'родительская директория'
SIZE = 'размер'
TYPE = 'тип'
NAME = 'имя'
SUBSID = 'дочерний объект'

THIS_FILE = 'file'
THIS_DIR = 'dir'

# path = 'C:\\Users\93139\OneDrive\Рабочий стол\espanol'

# print(os.listdir(path))
# for i in os.listdir(path):
#     print(i, type(i), path + '\\' + i, os.path.isdir(path + '\\' + i))
#     print(i, type(i), path + '\\' + i, os.path.isfile(path + '\\' + i))

# def search_file(path, level=1):
#     print('level= ', level, 'Content: ', os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path + '\\' + i):
#             print('Спускаемся', path + '\\' + i)
#             search_file(path + '\\' + i, level + 1)
#             print('Возвращаемся', path)
#
# search_file(path)

def save_to_json(info: dict, file_name: str):
    with open(file_name, "w") as f:
        json.dump(info, f, indent=2)

def save_to_csv(info: dict, file_name: str):
    with open(file_name, "w", encoding="UTF-8", newline='') as f:
        csw_writer = csv.DictWriter(f, dialect='excel', quoting=csv.QUOTE_MINIMAL,
                                    fieldnames=[MAIN, NAME, SIZE, TYPE])
        csw_writer.writeheader()
        dict_info = []
        dict_info(info, dict_info)

        csw_writer.writerows(dict_info)


def save_to_picle(info: dict, file_name: str):
    with open(file_name, "wb") as f:
        pickle.dump(info, f)


def dir_info(path: str = None) -> dict:
    start_path = Path().cwd() if path is None else Path(path)
    return file_info(start_path)

def dict_info(info: dict, list_info: list) -> list:
    csv_dict = {
        MAIN: info.get(MAIN, ""),
        NAME: info.get(NAME, ""),
        TYPE: info.get(TYPE, ""),
        SIZE: info.get(SIZE, 0)
    }
    list_info.append(csv_dict)
    list_sub = info.get(SUBSID, None)
    if list_sub is not None:
        for c in list_sub:
            dict_info(c, list_info)
    return list_info


def file_info(file: Path) -> dict:
    info = {MAIN: file.parent.name, NAME: file.name}
    if file.is_file():
        info[SIZE] = file.stat().st_size
        info[TYPE] = THIS_FILE
    else:
        info[TYPE] = THIS_DIR
        info[SIZE] = 0
        list_sub = []
        for p in file.iterdir():
            sub = file_info(p)
            info[SIZE] += sub.get(SIZE, 0)
            (list_sub.append(sub))
        info[SUBSID] = list_sub

    return info


if __name__ == '__main__':
    print(dir_info())
