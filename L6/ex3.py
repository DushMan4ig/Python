from random import randint
minimal = int(input('Введите минимальное число: '))
maximal = int(input('Введите максимальное число: '))
print(my_list :=[randint(minimal, maximal) for _ in range(10)])
kol = 0
for i in set(my_list):
    kol += my_list.count(i) // 2
print(kol)