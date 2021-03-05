a = int(input("enter the start of the range: "))
b = int(input("enter the end of the range: "))
n = int(input("enter the number : "))
if n in range(a, b):
    print(f"{n} is in the range{a, b}")
else:
    print("The number is outside the given range.")



