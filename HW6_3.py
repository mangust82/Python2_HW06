# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import randint
from Games import qeens


def gen_queens() -> list[tuple[int,int]]:
    num = 0
    while num != 4:
        q_pos = [(1,randint(1,8)), (2,randint(1,8)), (3,randint(1,8)),\
                 (4,randint(1,8)), (5,randint(1,8)), (6,randint(1,8)),\
                 (7,randint(1,8)), (8,randint(1,8))]
        # print(randint(1,8))
        if qeens.check_position(q_pos):
            print(q_pos)
            num += 1


if __name__ == '__main__':
    gen_queens()
