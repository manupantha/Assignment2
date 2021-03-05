lst = [1, 2, 4, 6, 2, 1]
list1 = []
for i in lst:
    if i not in list1:
        list1.append(i)

print(list1)
