# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.
SYSTEM_NUMBER = 16
DELIMITER = 10


def translation_system(num):
    hex_num = ''
    while num > 0:
        remainder = num % SYSTEM_NUMBER
        if remainder < DELIMITER:
            hex_num = str(remainder) + hex_num
        else:
            hex_num = chr(ord('A') + remainder - DELIMITER) + hex_num
        num //= SYSTEM_NUMBER
    return hex_num


num_input = int(input('Введите число: '))
print(translation_system(num_input))
print(hex(num_input))
