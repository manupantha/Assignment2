lst = []
n = int(input("Enter number of elements : "))
for i in range(n):
    ele = int(input())
    lst.append(ele)
print("the list is: ", lst)
mul=1
for x in lst:
    mul=mul*x
print("multiple of the list is: ", mul)
