# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number = int(input('Введите номер билета: '))

digit_6 = number % 10
number = number // 10

digit_5 = number % 10
number = number // 10

digit_4 = number % 10
number = number // 10

digit_3 = number % 10
number = number // 10

digit_2 = number % 10
number = number // 10

digit_1 = number % 10

FirstPart = digit_1 + digit_2 + digit_3
SecondPart = digit_4 + digit_5 + digit_6

if FirstPart == SecondPart:
    print('Билет счастливый')
else:
    print('Билет обычный')