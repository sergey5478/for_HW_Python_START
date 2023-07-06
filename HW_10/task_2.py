"""Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки."""


class Animal:
    """Родительский класс"""

    def __init__(self, weight):
        self.weight = weight


class Lion(Animal):
    """Вес и свойство животного"""
    loc = {1: 'S_Africa', 2: 'N_Africa'}

    def __init__(self, weight, lion_location):
        self.king = lion_location
        super().__init__(weight)

    def info_lion(self):
        """Возвращает свойство животного"""
        return self.loc[self.king]


class Panther(Animal):
    """Вес и свойство животного"""
    loc = {1: 'black', 2: 'white'}

    def __init__(self, weight, cat_color):
        self.cat = cat_color
        super().__init__(weight)

    def info_panther(self):
        """Возвращает свойство животного"""
        return self.loc[self.cat]


class Camel(Animal):
    """Вес и свойство животного"""
    loc = {1: '1_hump ', 2: '2_hump '}

    def __init__(self, weight, hump):
        self.hump = hump
        super().__init__(weight)

    def info_camel(self):
        """Возвращает свойство животного"""
        return self.loc[self.hump]


if __name__ == '__main__':
    my_lion = Lion(55, 2)
    my_panther = Panther(66, 1)
    my_camel = Camel(106, 2)
    print(my_lion.info_lion(), my_panther.info_panther(), my_camel.info_camel())
