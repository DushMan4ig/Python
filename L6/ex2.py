from random import randint
my_list = [randint(0, 10) for _ in range(15)]
kol = 0
for i in range(1, len(my_list) - 1):
    if my_list[i - 1] < my_list[i] > my_list[i + 1]:
        kol += 1
if my_list[-1] < my_list[0] > my_list[1]:
    kol += 1
elif my_list[0] < my_list[-1] > my_list[-2]:
    kol += 1
print(my_list)
print(kol)
