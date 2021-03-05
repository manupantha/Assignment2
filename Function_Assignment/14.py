my_dict = {}
n = int(input("enter the number of element : "))
for i in range(n):
    key = int(input("enter the key: "))
    value = int(input("enter the value: "))
    my_dict.update({key: value})
print(my_dict)


def sortbyvalue():
    sortedvalue = sorted(my_dict.items(), key=lambda x: x[1])
    return sortedvalue


print(my_dict(sortbyvalue()))
