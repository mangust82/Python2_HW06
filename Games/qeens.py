# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

__all__ = ['line_f', 'check_position']

queens = [(1,1), (2,4), (3,2), (1,5), (5,3), (6,7), (7,5), (8,8)]
# queens = [(1,3), (2,7), (3,2), (4,8), (5,5), (6,1), (7,4), (8,6)]


def line_f(qeen: tuple[int, int]) -> set[tuple[int,int]]:
    """
    the function searches for the set of coordinates that the queen hits along the diagonals
    :param qeen: tuple of int numbers
    :return: set of tuple of int
    """
    k1 = qeen[1] - qeen[0]
    k2 = qeen[1] + qeen[0]
    m1 = {(x, x + k1) for x in range(1,9) if 1 <= x + k1 <= 8 and x != qeen[0]}
    m2 = {(x, k2 - x) for x in range(1, 9) if 1 <= k2 - x <= 8 and x != qeen[0]}
    all_m = m1.union(m2)
    return all_m


def check_position(queens: list[tuple[int,int]]) -> bool:
    """
    Function  checks vertical horizontal and diagonal position of the queens to each other.

    :param queens: list of tuple of int numbers
    :return: bool     
    """
    x_set = {queens[i][0] for i in range(0,8)} #проверяем стоят ли ферзи на одной вертикали или горизонтали по длине множества если стоят то координаты совпадают и множество уменьшается на одно значение.
    y_set = {queens[i][1] for i in range(0,8)}
    if len(x_set)<8 or len(y_set)<8:
        return False
    else:
        for i in range(0,8):
            new_list = queens.copy()
            new_list.pop(i)
            Test = set(new_list).intersection(line_f(queens[i]))
            if len(set(new_list).intersection(line_f(queens[i]))) == 0: # проверяем есть ли координата ферзя среди координат битой диагонали другого ферзя. Если пересечений множеств нет то ферзи не бьются.
                flag = 1
            else:
                return False
        if flag:
            return True


if __name__ == '__main__':
    print(f'Ферзи не бьют друг друга' if check_position(queens) else f'Ферзи бьют друг друга')
