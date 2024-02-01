__all__ = ['input_user', 'json_to_csv', 'csv_two_json', 'json_to_pickle', 'pickle_2_csv', 'csv_2_pickles']

from pathlib import Path
import json
import csv
import pickle


def input_user(path: Path) -> None:
    unique_id = set()
    if not path.is_file():
        data = {str(level): {} for level in range(1, 8)}
    else:
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            #unique_id = {id for id_name in data.values() for id in id_name.keys()}
            for id_name in data.values():
                unique_id.update(id_name.keys())

    while name := input('enter the name of user: '):
        level = input('enter level from 1 to 7: ')
        user_id = input('enter id: ')
        if user_id not in unique_id:
            unique_id.add(user_id)
            data[level].update({user_id: name})
            with open(path, 'w', encoding='utf-8') as f_write:
                json.dump(data, f_write, indent=4, ensure_ascii=False)
        else:
            print('such id is already exist')

if __name__ == '__main__':
    input_user(Path('users.json'))


def json_to_csv(path: Path)-> None:
    with open(path, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)

    result = []
    for level, id_name in data.items():
        for id, name in id_name.items():
            result.append({'level': int(level), 'id': int(id), 'name': name})
    with open(path.stem + '.csv', 'w', encoding='utf-8', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(result)

if __name__ == '__main__':
    json_to_csv(Path('users.json'))

def csv_two_json(from_path: Path, to_path: Path) -> None:
    result = []
    with open(from_path, 'r', encoding='utf-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, row in enumerate(csv_read):
            if i != 0:
                level, id, name = row
                data = {
                    'level': int(level),
                    'id': f'{int(id):010}',
                    'name': name.title(),
                    'hash': hash(f'{name.title()}{int(id):010}')
                }
                result.append(data)
    with open(to_path, 'w', encoding='utf-8') as f_write:
        json.dump(result, f_write, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    csv_two_json(Path('users.csv'), Path('new_users.json'))

def json_to_pickle(path: Path) -> None:
    for obj in path.iterdir():
        if obj.is_file() and obj.suffix == '.json':
            with(
                open(obj, 'r', encoding='utf-8') as f_read,
                open(obj.stem + '.pickle', 'wb') as f_write
            ):
                data = json.load(f_read)
                pickle.dump(data, f_write)

if __name__ == '__main__':
    json_to_pickle(Path(r'C:\Users\93139\PycharmProjects\pythonProject2'))


def pickle_2_csv(path: Path) -> None:
    with open(path, 'rb') as f_read:
        data = pickle.load(f_read)
    headers = list(data[0].keys())
    with open(path.stem + '.csv', 'w', encoding='utf-8', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=headers, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)

if __name__ == '__main__':
    pickle_2_csv(Path('new_users.pickle'))


def csv_2_pickles(path: Path) -> None:
    with open(path, 'r', encoding='utf-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel')
        result = []

        #print(*csv_read)
        for i, row in enumerate(csv_read):
            if i != 0:
                result.append(print(dict(zip(headers, row))))
            else:
                headers = row

    print(pickle.dumps(result))

if __name__ == '__main__':
     csv_2_pickles(Path('users.csv'))