l1 = input("Enter the elements of array 1 : ")
s1 = l1.split(',')
for i in range(len(s1)):
    s1[i] = int(s1[i])
print(f"array1 : {s1}")
l = input("Enter the elements of array 2 : ")
s2 = l.split(',')
for i in range(len(s2)):
    s2[i] = int(s2[i])
print(f"array2 : {s2}")

result = list(filter(lambda x: x in s1, s2))
print("Intersection of the said arrays: ", result)
