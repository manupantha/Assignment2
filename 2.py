str = input("enter the string")
if len(str) < 2:
    print("empty string")
else:
    print(str[0:2] + str[-2:])
