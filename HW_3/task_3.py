"""None"""
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Верните все возможные варианты комплектации рюкзака.
import itertools

MY_DICT = {'салфетки': 1, 'спички': 2, 'крючки': 3, 'носки': 4, 'зажигалка': 5,
           'нож': 6, 'вилка': 7, 'ложка': 8, 'миска': 9, 'котелок': 10, 'плед':
               11, 'бинокль': 12, 'фонарик': 13}
MAX_WEIGHT = 20

my_combinations = []

for index in range(1, len(MY_DICT) + 1):
    for combo in itertools.combinations(MY_DICT.items(), index):
        total_weight = sum(value for _, value in combo)
        if total_weight == MAX_WEIGHT:
            my_combinations.append(combo)
for combo in my_combinations:
    print(combo)
