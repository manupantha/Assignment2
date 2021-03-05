lst = []
n = int(input("enter the number of elements: "))
for i in range(n):
    elements = input("number: ")
    lst.append(elements)
print("the list is: ", lst)
count = 0
for string2 in lst:
    if len(string2) > 1 and string2[0] == string2[-1]:
        count += 1
print(count)
