from random import randint
count_water = int(input('Введите количество арбузов: '))
min_water = float('inf')
max_water = float('-inf')
for i in range(count_water):
    weigth = randint(1, 50)
    print(weigth)
    if weigth < min_water:
        min_water = weigth
    if weigth > max_water:
        max_water = weigth
print(min_water, max_water)
        
    