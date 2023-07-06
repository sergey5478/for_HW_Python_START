"""Класс принимает тип животного (название одного из созданных классов) и
параметры для этого типа. Внутри класса создайте экземпляр на основе переданного
типа и верните его из класса-фабрики."""
from task_2 import Lion


class MyClass:
    """Принимает клас и его атрибуты"""

    def __init__(self, animal_class, weight, lion_location):
        self.animal = animal_class(weight, lion_location)

    def call_method(self):
        """Возвращает информацию о Lion"""
        return self.animal.info_lion()


WEIGHT = 200
LION_LOCATION = 1

if __name__ == '__main__':
    my_instance = MyClass(Lion, WEIGHT, LION_LOCATION)
    print(my_instance.call_method())
