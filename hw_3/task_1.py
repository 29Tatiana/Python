# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов

numbers = [1, 339, 559, 7, 44, 339, 7]
dup_numbers = []
res= []
for elem in set(numbers):
    if numbers.count(elem) > 1:
        dup_numbers.append(elem)
    else:
        res.append(elem)

print(f"Список дублирующихся элементов: \n{dup_numbers}")
print(f"Результирующий список (без дубликатов): \n{res}")
