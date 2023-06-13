"""✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь."""


def calculate_profit_loss(companies):
    """Выбираем все значения, суммируем и добавляем в список"""
    profit_loss = []
    for _, data in companies.items():
        revenues = sum(data)
        profit_loss.append(revenues)
    return all(x > 0 for x in profit_loss)


dict_companies = {'Company A': [100, -500, 200], 'Company B': [150, -100, 120]}
print(calculate_profit_loss(dict_companies))
