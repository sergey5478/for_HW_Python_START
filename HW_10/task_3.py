"""Возьмите любую из задач с прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра."""
import json
import pickle
import os


class MyClass:
    """Класс принимает текущий рабочий каталог """

    def __init__(self, directory):
        self.directory = directory

    def convert_json_to_pickle(self):
        """Смотрит файлы json и переписывает в pickle"""
        json_files = [i for i in os.listdir(self.directory) if i.endswith('.json')]
        for json_file in json_files:
            with open(os.path.join(self.directory, json_file), 'r', encoding='utf-8') as f_json:
                with open(os.path.join(self.directory, json_file.rstrip('.json') + '.pickle'),
                          'wb') as f_p:
                    pickle.dump(json.load(f_json), f_p)


if __name__ == '__main__':
    my_instance = MyClass(os.getcwd())
    my_instance.convert_json_to_pickle()
