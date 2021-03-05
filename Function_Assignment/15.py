from functools import reduce

list1 = input("enter the list: ")
split1 = list1.split(',')
for i in range(0, len(split1)):
    split1[i] = int(split1[i])
print(split1)
string1 = lambda x: x / 2 > 0
result = filter(string1, split1)
print(list(result))
