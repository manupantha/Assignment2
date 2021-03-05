lst = []
n = int(input("enter the number of elements: "))
for i in range(n):
    elements = int(input("number: "))
    lst.append(elements)
print("the list is: ", lst)
print("the smallest number among the list is: ", min(lst))
