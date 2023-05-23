# Решение 1
# dist = int(input('Сколько машина проезжает за день: '))
# total = int(input('Сколько надо проехать: '))

# print(f'Машине понадобится {(total + dist - 0.1) // dist} дня')

dist = int(input('Сколько машина проезжает за день: '))
total = int(input('Сколько надо проехать: '))
print(f'Машине понадобится {total // dist + (total % dist > 0)} дня')
print(total % dist > 0)