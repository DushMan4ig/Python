N = int(input('Введите колличество элементов в массиве: '))

A = list(map(int, input('Введите элементы массива: ').split()))

X = int(input('Введите число Х: '))

count = 0

for num in A:
    if num == X:
        count += 1

print(f'Число Х встречается {count} раз')