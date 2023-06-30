"""Задание №7.
Прочитайте созданный в прошлом задании csv файл без
использования csv. DictReader.
Распечатайте его как pickle строку."""
import csv
import pickle


def read_csv_to_pickle(csv_file):
    """Открываем, читаем, распечатываем"""
    with open(csv_file, 'r', newline='', encoding='utf-8') as my_file:
        data = list(csv.reader(my_file))

    pickle_data = pickle.dumps(data)
    return pickle_data


print(read_csv_to_pickle('data.csv'))
