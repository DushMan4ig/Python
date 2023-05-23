# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

Integer = int(input('Введите число: '))
Sotni = Integer // 100
Des = (Integer // 10) - ((Integer // 100) * 10)
Edinicy = Integer % 10
Itog = Sotni + Des + Edinicy
print(f'Сумма цифр введенного числа равна : {Itog}')
