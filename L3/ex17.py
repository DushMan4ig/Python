# from random import randint
# lis = list()
# lens = int(input('Введите длину строки: '))
# for i in range(lens):
#     lis.append(randint(0, 10))
# print(lis)
# numbers = 0
# for i in range (len(lis)):
#     for j in range (len(lis)):
#         if j != i:
#             numbers += 1
# print(numbers)
    
import random
from random import randint

my_list = []
for __ in range(10):
    my_list.append(random.randint(0, 10))
print(my_list)

# my_list = set(my_list)
# print(my_list)
# print(len(my_list))

uniq_list = []
for item in my_list:
    if item not in uniq_list:
        uniq_list.append(item)
print(uniq_list)
