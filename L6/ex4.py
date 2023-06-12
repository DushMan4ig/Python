my_list_summa = []
my_list_summa1 = []
for i in range(2,284 + 1):
    for j in range (1, i):
        if i % j == 0:
            my_list_summa.append(i)
            for g in range(1, sum(my_list_summa)):
                if sum(my_list_summa) % 2== 0:
                    my_list_summa1.append(g)
    if sum(my_list_summa1) == i:
        print(i, my_list_summa1)
        