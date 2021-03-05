from functools import reduce

l1 = input("enter the list: ")
l2 = l1.split(',')
for i in range(len(l2)):
    l2[i] = int(l2[i])
print(l2)

mul = lambda x, y: x * y
r = reduce(mul, l2)
print(f"Product is: {r}")
