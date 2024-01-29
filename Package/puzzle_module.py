
__all__ = ['puzzle', 'puzzl_stor']

def puzzle(puzzle:str, answers:list[str], counter:int=3) -> int:
    print('Отгадайте загадку: ')
    print(f'{puzzle}')
    for i in range(counter):
        answer = input('Введите ответ: ').lower()
        if answer in answers:
            print('Поздравляем, отгадали!')
            return i + 1
    print('Не угадали:(')
    return 0

if __name__ == '__main__':
    puzzle('Зимой и летом одним цветом', ['ель', 'елка', 'сосна'])

_data = {}
def puzzl_stor():
    storage = {
        'Зимой и летом одним цветом': ['ель', 'елка', 'сосна', 'дуб'],
        'не лает не кумает в дом не пускает': ['замок', 'засов', 'домофон'],
        'висит груша нельзя скушать': ['лампа', 'лампочка', 'тетя']
    }
    for k, v in storage.items():
        res = puzzle(k, v)
        print('Не угадали' if not res else f'Вы угалали с {res} попытки')

def save_res(text, num):
    _data[text] = num

def show_res(data):
    for k, v in data.items():
        print(f'загадку {k} не угадали' if not res else f'вы угадали загадку {k} c {v} попытки')

if __name__ == '__main__':
    puzzl_stor()