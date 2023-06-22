""" Задача7.
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате
DD.MM.YYYY. Функция возвращает истину, если дата может существовать или ложь, если такая дата
невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
Задача8.
Добавьте в __init__ пакета имена модулей внутри дандер __all__.
В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за
пределами модуля.

Домашнее задание1.
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
from sys import argv


def is_valid_date(date_str):
    """Проверки"""
    day, month, year = map(int, date_str.split('.'))

    if not is_valid_year(year):
        return False

    if month < 1 or month > 12:
        return False

    days_in_month = get_days_in_month(month, year)
    if day < 1 or day > days_in_month:
        return False

    return True


def is_valid_year(year):
    """Год"""
    if year < 1 or year > 9999:
        return False

    return True


def get_days_in_month(month, year):
    """Дни"""
    if month == 2 and _is_leap_year(year):
        return 29
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def _is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


__all__ = ['is_valid_date', 'is_valid_year', 'get_days_in_month']
if __name__ == '__main__':
    *_, date = argv
    print(is_valid_date(date))

# python task_1.py 29.02.2024
