my_dict = [{"V": "S001"},
           {"V": "S002"},
           {"V": "S003"},
           {"V": "S004"},
           {"V": "S005"},
           {"V": "S006"},
           {"V": "S007"},
           {"V": "S001"}]
my_list = []
for i in range(len(my_dict)):
    my_list += my_dict[i].values()
print(list(my_list))