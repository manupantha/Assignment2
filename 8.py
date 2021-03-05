def remove_char(string1, n):
    first_part = string1[:n]
    last_part = string1[n + 1:]
    return first_part + last_part


print(remove_char(input("enter the string"), int(input("enter the index"))))
