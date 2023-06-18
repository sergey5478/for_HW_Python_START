"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""
import os


def file_path_os(file_path):
    """С помощью os"""
    name = os.path.basename(file_path)
    extension = os.path.splitext(name)[1]
    return file_path, name, extension


MY_FILE_PATH = r"C:\APython\Git projects\for_HW_Python_START\HW_4\transactions.txt"
print(file_path_os(MY_FILE_PATH))


def parse_file_path(file_path):
    """Второй способ"""
    *_, name = file_path.split('\\')
    return file_path, name, '.' + name.split('.')[1]


print(parse_file_path(MY_FILE_PATH))
