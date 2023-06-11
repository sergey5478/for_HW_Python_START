"""None."""
# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
list_new = [1, 2, 3, 4, 5, 1, 2, 3]
res = set()
for value in set(list_new):
    if list_new.count(value) > 1:
        res.add(value)

print(res)
