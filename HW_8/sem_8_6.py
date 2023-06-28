"""Задание №6.
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv-файл.
Для тестирования возьмите pickle версию файла из предыдущей задачи
этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import csv
import pickle


def pickle_to_csv(pickle_file, csv_file):
    """Открываем, проверяем записываем"""
    with open(pickle_file, 'rb') as pickle_f:
        data = pickle.load(pickle_f)

    if not data:
        return 0

    keys = data[0].keys()

    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


pickle_to_csv('user.pickle', 'data.csv')
