# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes

arr = [4, 9, 2, 5, 1, 8, 7]
min_val = 2
max_val = 6

result = find_indexes(arr, min_val, max_val)
print("Индексы элементов, значения которых находятся в заданном диапазоне:")
print(result)