"""Создайте исключения."""


def make(my_number, num_attempts):
    """NONE"""

    def game():
        attempt = 0
        while attempt < num_attempts:
            attempt += 1
            try:
                user_number = int(input(f'Попытка номер {attempt}. Введите число: '))
            except ValueError:
                print('Вы ввели некорректное значение. Введите целое число.')
                continue

            if user_number < my_number:
                print('Вы вводите меньше')
            elif user_number > my_number:
                print('Вы вводите больше')
            else:
                print(f'Вы отгадали с {attempt} попытки!')
                return True
        else:
            print(f'Вы использовали все {attempt} попыток и не отгадали число. '
                  f'Было загадано число {my_number}. Вы проиграли.')
            return False

    return game


if __name__ == '__main__':
    NUMBER = 10
    NUM_OF_ATTEMPTS = 5
    res = make(NUMBER, NUM_OF_ATTEMPTS)
    res()
