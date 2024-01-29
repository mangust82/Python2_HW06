# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число
# (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


_my_dict = {}
__all__ = ['list_puzzle', 'puzzle1']

def puzzle1(puzzle: str, replies: list[str], attempt:int=3) -> int:
    print(puzzle)

    for i in range(attempt):
        answer = input("Ответ:")
        if answer in replies:
            print('Угадали')
            return i+1
        else:
            print('Попробуйте ещё раз')
    return 0


def list_puzzle() -> None:
    dict_puzzle = {"Зимой и летом одним цветом": ["ель", "елка", "ёлка", "сосна"],
    "Не лает, не кусает, в дом не пускает": ["замок", "засов", "домофон"],
    "Висит груша, нельзя скушать": ["лампа", "лампочка", "светильник"]
    }

    for puzzle, replies in dict_puzzle.items():
        res = puzzle1(puzzle, replies)
        print('Не угадли ни с одной попытки' if not res else f'вы угадали с {res} попытки')
        attempt(puzzle, res)



def attempt(guess: str, num_at: str) -> dict:
    # my_dict.update({guess:num_at})
    _my_dict[guess] = num_at
    # return my_dict


def print_guess() -> None:
    log = [f'Загадку {guess} не угадали \n' if not atempt else f'Вы угадали загадку {guess} с {atempt} попытки \n' for guess, atempt in _my_dict.items() ]
    print(*log)

if __name__ == '__main__':
    list_puzzle()
    print_guess()