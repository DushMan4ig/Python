stroka = str(input('Введите строку: '))
my_list = list(stroka)
kol = 0
for i in range(len(my_list)):
    for j in range(len(my_list)):
        if my_list[i] == my_list[j]:
            kol += 1
            stroka
        