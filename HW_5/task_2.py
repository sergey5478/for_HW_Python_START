"""✔ Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии."""


def create_dict(arg_1, arg_2, arg_3):
    """Однострочный генератор словаря"""
    dict_bonus = {arg_1[i]: arg_2[i] * float(arg_3[i].replace('%', '')) for i in range(len(arg_1))}
    return dict_bonus


names = ['Kisa', 'Den', 'Tom']
rate = [1000, 2000, 3000]
bonus = ['1.1%', '1.2%', '1.3%']

print(create_dict(names, rate, bonus))
