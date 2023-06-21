"""Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
расстановки ферзей в задаче выше. Проверяйте различные случайные варианты и выведите
4 успешных расстановки."""
import itertools


def generate_queen_arrangements():
    """Цифры это строки, индексы столбцы"""
    arrangements = []
    for queens in list(itertools.permutations(range(8))):
        if all(queens[col_1] != queens[col_2] + (col_2 - col_1) and queens[col_1] != queens[col_2]
               - (col_2 - col_1) for col_1, col_2 in itertools.combinations(range(8), 2)):
            arrangements.append(queens)
    return arrangements


successful_arrangements = generate_queen_arrangements()
for i, arrangement in enumerate(successful_arrangements, 1):
    if isinstance(arrangement, int):
        arrangement = [arrangement]
    print(f"Расстановка {i}: {[(row + 1, col + 1) for row, col in enumerate(arrangement)]}")
