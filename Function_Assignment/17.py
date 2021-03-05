char1 = input("Enter a character: ")
string1 = input("Enter a string: ")

char2 = list(filter(lambda x: x.startswith(char1), string1))
not_start = list(filter(lambda x: not x.startswith(char1), string1))
if char2:
    print(f"The string with given character {char1} is: {string1}")
else:
    print(f"The string with given character {char1} is not in string: {string1}")
