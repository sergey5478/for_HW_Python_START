"""Напишите следующие функции:
Нахождение корней квадратного уравнения.
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения
с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""
import math
import csv
import random
import json

MAX_LINES = 1000
MIN_LINES = 100
RANDOM_NUMBERS = 3
RANDOM_COUNT = 20


def generate_csv_file(filename):
    """Генерация CSV файла с тремя случайными числами."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=':')
        for _ in range(random.randint(MIN_LINES, MAX_LINES)):
            row = [random.randint(RANDOM_NUMBERS, RANDOM_COUNT) for _ in range(RANDOM_NUMBERS)]
            writer.writerow(row)


def quadratic_equation_solver(arg_1, arg_2, arg_3):
    """Функция для решения квадратного уравнения вида ax^2 + bx + c = 0."""
    discriminant = arg_2 ** 2 - 4 * arg_1 * arg_3
    if discriminant > 0:
        root_1 = (-arg_2 + math.sqrt(discriminant)) / (2 * arg_1)
        root_2 = (-arg_2 - math.sqrt(discriminant)) / (2 * arg_1)
        return root_1, root_2
    if discriminant == 0:
        root = -arg_2 / (2 * arg_1)
        return root
    else:
        return None


def quadratic_solver_decorator(func):
    """Декоратор, передающий данные из random_numbers.csv в функцию вычисления корней."""

    def wrapper(filename):
        data = []
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=':')
            for row in reader:
                arg_a, arg_b, arg_c = map(int, row)
                result = func(arg_a, arg_b, arg_c)
                data.append({
                    'a': arg_a,
                    'b': arg_b,
                    'c': arg_c,
                    'roots': result
                })
        return data

    return wrapper


def save_to_json(filename):
    """Декоратор, сохраняющий всё в JSON файл."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(result, file, indent=4)
            return result

        return wrapper

    return decorator


@save_to_json("roots.json")
@quadratic_solver_decorator
def solve_quadratic_equation(arg1, arg2, arg3):
    """None"""
    return quadratic_equation_solver(arg1, arg2, arg3)


if __name__ == '__main__':
    generate_csv_file("random_numbers.csv")
    solve_quadratic_equation("random_numbers.csv")
