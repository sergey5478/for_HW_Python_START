"""Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
"""
import os
import json
import csv
import pickle


def get_directory_info(directory):
    """Проверка файл или директория, запись в результат"""
    result = []

    for entry in os.scandir(directory):
        if entry.is_file():
            file_info = {
                'name': entry.name,
                'type': 'file',
                'size': entry.stat().st_size,
                'parent_directory': os.path.relpath(directory),
            }
            result.append(file_info)
        elif entry.is_dir():
            subdirectory_info = get_directory_info(entry.path)
            directory_size = sum(item['size'] for item in subdirectory_info) + entry.stat().st_size

            directory_info = {
                'name': os.path.relpath(entry.path, directory),
                'type': 'directory',
                'size': directory_size,
            }
            result.append(directory_info)
            result.extend(subdirectory_info)

    return result


def save_to_json(result, output_file):
    """Запись в файл"""
    with open(output_file, 'w', encoding='utf-8') as f_json:
        json.dump(result, f_json, ensure_ascii=False, indent=2)


def save_to_csv(result, output_file):
    """Запись в файл"""
    with open(output_file, 'w', newline='', encoding='utf-8') as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=['name', 'type', 'size', 'parent_directory'])
        writer.writeheader()
        writer.writerows(result)


def save_to_pickle(result, output_file):
    """Запись в файл"""
    with open(output_file, 'wb') as f_pickle:
        pickle.dump(result, f_pickle)


def process_directory(directory):
    """Main))"""
    result = get_directory_info(directory)

    json_file = 'result.json'
    csv_file = 'result.csv'
    pickle_file = 'result.pickle'

    save_to_json(result, json_file)
    save_to_csv(result, csv_file)
    save_to_pickle(result, pickle_file)


if __name__ == '__main__':
    MY_DIRECTORY = 'ktest2'
    process_directory(MY_DIRECTORY)
