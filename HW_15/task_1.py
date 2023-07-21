"""Напишите код, который запускается из командной строки и
получает на вход путь до директории на ПК. Соберите информацию
о содержимом в виде объектов namedtuple.
Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование."""
import os
import logging
import collections
import sys

logging.basicConfig(filename='directory_info.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

FileInfo = collections.namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent'])


def gather_directory_info(my_directory_path, use_directory_flag=False):
    try:
        dir_info = []
        abs_path = os.path.abspath(my_directory_path)
        for item_in_dir in os.listdir(my_directory_path):
            item_path = os.path.join(abs_path, item_in_dir)
            name, extension = os.path.splitext(item_in_dir)
            if use_directory_flag:
                is_directory = os.path.isdir(item_path)
            else:
                is_directory = None
            parent_dir = os.path.basename(abs_path)
            dir_info.append(FileInfo(name, extension[1:], is_directory, parent_dir))
        return dir_info

    except Exception as e:
        logging.exception("Error while gathering directory information:")
        raise e


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    directory_path = sys.argv[1]
    try:
        directory_info = gather_directory_info(directory_path, use_directory_flag=True)
        for item in directory_info:
            print(item)
        with open('directory_info.txt', 'a', encoding='utf-8') as file:
            for item in directory_info:
                file.write(str(item) + '\n')

    except Exception as e:
        print("Error occurred.")
