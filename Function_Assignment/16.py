l1 = input("Enter a list: ")
l1_s = l1.split(',')
for i in range(len(l1_s)):
    l1_s[i] = int(l1_s[i])
print(f"Given list : {l1_s}")

square = lambda x:x**2
cube = lambda x:x**3

res1 = list(map(square,l1_s))
res2 = list(map(cube,l1_s))

print(f"Square of given list: {res1}")
print(f"Cube of given list: {res2}")


square = lambda x:x**2
cube = lambda x:x**3
