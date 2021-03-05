def prepend(list1, str):
    str += '% s'
    list1 = [str % i for i in list1]
    return list1


list2 = [1, 2, 3, 4]
str1 = 'emp'
print(prepend(list2, str1))
