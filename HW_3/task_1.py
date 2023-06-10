"""None."""
# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
list_new = [1, 2, 3, 4, 5, 1, 2, 3]
res = []
for value in list_new:
    if list_new.count(value) > 1 and value not in res:
        res.append(value)

print(res)
