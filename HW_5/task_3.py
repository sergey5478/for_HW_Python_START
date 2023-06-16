"""✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


def fibonacci_generator():
    """Многострочный генератор числа Фибоначчи"""
    number_a, number_b = 0, 1
    while True:
        yield number_a
        number_a, number_b = number_b, number_a + number_b


fib = fibonacci_generator()
for _ in range(5):
    print(next(fib))
