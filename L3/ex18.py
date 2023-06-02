N = int(input('Введите количество элементов в массиве: '))

A = list(map(int, input('Введите элементы массива: ').split()))

X = int(input('Введите число Х: '))

closest_index = 0

closest_diff = abs(A[0] - X)

for i in range(1, N):
    diff = abs(A[i] - X)
    if diff < closest_diff:
        closest_index = i
        closest_diff = diff

print(A[closest_index])