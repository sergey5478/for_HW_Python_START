"""Напишите функцию, принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление."""


def create_argument_dictionary(**kwargs):
    """Принимает ключи и проверяет на наличие хэша, через функцию hashable"""
    argument_dict = {}
    for key, value in kwargs.items():
        if hashable(key):
            argument_dict[value] = key
        else:
            argument_dict[str(value)] = key
    return argument_dict


def hashable(obj):
    """Проверка на наличие хэша"""
    try:
        hash(obj)
        return True
    except TypeError:
        return False


print(create_argument_dictionary(arg1='Hello', arg2='25.25', arg3=42))
