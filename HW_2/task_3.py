# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions


def parse_fraction(fraction_str):
    parts = fraction_str.split('/')
    numerator = int(parts[0])
    denominator = int(parts[1])
    return numerator, denominator


def sum_mult(fraction_1, fraction_2):
    numerator_1, denominator_1 = parse_fraction(fraction_1)
    numerator_2, denominator_2 = parse_fraction(fraction_2)
    common_denominator = denominator_1 * denominator_2

    # Сложение
    sum_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1
    sum_fraction = f"{sum_numerator}/{common_denominator}"

    # Умножение
    prod_numerator = numerator_1 * numerator_2
    prod_denominator = denominator_1 * denominator_2
    prod_fraction = f"{prod_numerator}/{prod_denominator}"

    return sum_fraction, prod_fraction


fraction_a = input("Введите первую дробь в формате 'числитель/знаменатель': ")
fraction_b = input("Введите вторую дробь в формате 'числитель/знаменатель': ")

result_sum, result_prod = sum_mult(fraction_a, fraction_b)
print("Сумма:", result_sum)
print("Произведение:", result_prod)
a = fractions.Fraction(fraction_a)
b = fractions.Fraction(fraction_b)
suma = a + b
prod = a * b
print(suma, prod)
