def insert_string_middle(string1, string2):
    length = int(len(string1) / 2)
    print(string1[:length] + string2 + string1[length:])


print(insert_string_middle(input("string1"), input("string2")))
