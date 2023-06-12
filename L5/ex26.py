# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def power_recursive(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * power_recursive(a, b - 1)
    else:
        return 1 / power_recursive(a, -b)

a = float(input("Введите число A: "))
b = int(input("Введите степень B: "))

result = power_recursive(a, b)
print(f"Результат: {result}")