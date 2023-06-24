"""Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён."""
import os
import random
import string

MIN_NAME_LENGTH = 6
MAX_NAME_LENGTH = 30
MIN_FILE_SIZE = 256
MAX_FILE_SIZE = 4096


def create_files(directory, extension, num_files):
    """Проверка наличия директории, создание, проверка файлов в ней"""
    if not os.path.exists(directory):
        os.makedirs(directory)

    existing_files = os.listdir(directory)

    for _ in range(num_files):
        name_length = random.randint(MIN_NAME_LENGTH, MAX_NAME_LENGTH)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits,
                                           k=name_length)) + '.' + extension
        while file_name in existing_files:
            name_length = random.randint(MIN_NAME_LENGTH, MAX_NAME_LENGTH)
            file_name = ''.join(random.choices(string.ascii_letters + string.digits,
                                               k=name_length)) + '.' + extension

        file_size = random.randint(MIN_FILE_SIZE, MAX_FILE_SIZE)

        data = os.urandom(file_size)
        file_path = os.path.join(directory, file_name)

        with open(file_path, 'wb') as file:
            file.write(data)


def create_dif_files(directory, **kwargs):
    """Разбираем на ключи и значения"""
    for ext, num in kwargs.items():
        create_files(directory, ext, num_files=num)


create_dif_files(directory='seminar_120', txt=1, bin=2, png=1)
