from random import randint
days = int(input('Введите количество дней: '))
temp = 1
count = 0
total_days = 0

for i in range(days):
    temp += randint(-3, 3)
    print(temp) 
    
    if temp > 0:
        count += 1
        total_days += 1
    else:
        count = 1
    
if total_days < count:
    total_days = count
print(f'Оттепель длилась {total_days} дней')
        