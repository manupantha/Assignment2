def reverse_string(string1):
    str1 = ""
    for i in string1:
        str1 = i + str1
    return str1


string1 = input("enter the string: ")
print("The original string is: ", string1)
print("The reverse string is", reverse_string(string1))
