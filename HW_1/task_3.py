# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10

print("Угадайте число от", LOWER_LIMIT, "до", UPPER_LIMIT)
print("У вас есть", attempts, "попыток.")

for attempt in range(1, attempts + 1):
    guess = int(input("Попытка №{}: ".format(attempt)))

    if guess == num:
        print("Поздравляю! Вы угадали число.")
        break
    elif guess < num:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")

if guess != num:
    print("К сожалению, вы не угадали число. Загаданное число было:", num)