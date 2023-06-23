"""Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов.
* При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
"""
import os


def rename_files(directory, desired_name, source_extension, new_extension):
    """Переименование файлов"""
    files = os.listdir(directory)

    for position, filename in enumerate(files):
        if filename.endswith(source_extension):
            original_name = os.path.splitext(filename)[0]
            new_name = f"{original_name}_{desired_name}_{position + 1}.{new_extension}"
            original_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(original_path, new_path)


if __name__ == "__main__":
    rename_files("new_dir", "new", "txt", "docx")
