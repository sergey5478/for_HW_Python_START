"""✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""


def replace_with_none():
    """Если var_name оканчивается на 's' отрезаем и придаём старое значение"""
    new_values = {}
    for var_name, var_value in globals().items():
        if var_name.endswith("s") and var_name != "s":
            new_values[var_name[:-1]] = var_value
            new_values[var_name] = None

    globals().update(new_values)


books = ["Python", "Java", "C++"]
CAT = "Whiskers"
DOGS = 5
S = "single"
replace_with_none()
print(globals())
