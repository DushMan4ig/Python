from random import randint
my_list = [randint(0, 10) for i in range(15)]
my_list1 = [randint(0, 10) for i in range(5)]
my_list_final = []
for i in my_list:
    if i not in my_list1:
        my_list_final.append(i)
print(my_list)
print(my_list1)
print(my_list_final)    
