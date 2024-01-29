# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint
from sys import argv

__all__ = ['guess']

a,b,c = [int(argv[i]) for i in range(1,len(argv))]
print(a,b,c)

def guess(a:int=0, b:int=100, c:int=10) -> bool:
    # a,b,c = map(int, input('Введите 3 числа:').split())
    # a,b,c = 1, 100,5
    N = randint(a,b)

    # guess = int(input('Num:'))
    i = 0
    print(N)
    while i < c:
        guess = int(input('Num:'))
        if N > guess:
            print('more')
        elif N < guess:
            print('less')
        else:
            print('exelent')
            return True
            # break
        i += 1
    print("you are looser")
    return False

if __name__ == '__main__':
    guess(a,b,c)
    # param = argv[1:]
    # guess(*(int(item) for item in param))