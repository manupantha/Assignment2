my_dict1 = {1: 10, 2: 20}
my_dict2 = {3: 30, 4: 40}
my_dict3 = {5: 50, 6: 60}
my_dict4 = {}
for d in (my_dict1, my_dict2, my_dict3):
    my_dict4.update(d)
print(my_dict4)
