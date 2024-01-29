# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ['chek_date']

def chek_date(data: str) -> bool:
    day_31 = (1,3,5,7,8,10,12)
    day_30 = (4, 6, 9, 10)
    my_list = data.split('.')
    if int(my_list[1]) in day_31 and 0<int(my_list[0])<=31 and  1<int(my_list[2])<=9999:
        return True
    elif int(my_list[1]) in day_30 and 0 < int(my_list[0]) <= 31 and 1 < int(my_list[2]) <= 9999:
        return True
    elif int(my_list[1]) == 2 and 0 < int(my_list[0]) <= 28 and 1 < int(my_list[2]) <= 9999 and not _check_leap(my_list[2]):
        return True
    elif int(my_list[1]) == 2 and 0 < int(my_list[0]) <= 29 and 1 < int(my_list[2]) <= 9999 and _check_leap(my_list[2]):
        return True
    else:
        return False

def _check_leap(year: str) -> bool:
    int_year = int(year)
    return int_year % 4 == 0 and int_year % 100 != 0 or int_year % 400 == 0

# a = input('Введите: ')
# print(chek_date(a))