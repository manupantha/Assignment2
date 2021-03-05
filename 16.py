# creating an empty list 
lst = []
n = int(input("Enter number of elements : "))
for i in range(n):
    ele = int(input())
    lst.append(ele)  # adding the element
print(lst)
print(sum(lst))