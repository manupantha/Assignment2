lst = []
n = int(input("enter the length of the list: "))
for i in range(n):
    elements = int(input("element: "))
    lst.append(elements)
print(lst)
print("the largest number is: ", max(lst))
