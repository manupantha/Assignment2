str = input("enter the string")
char = str[0]
str = str.replace(char, '$')
str = char + str[1:]
print(str)
