def remove_odd_string(string1):
    result = ""
    for i in range(len(string1)):
        if i % 2 == 0:
            result = result + string1[i]
    return result


print(remove_odd_string(input("enter the string: ")))
