l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def function(data):
    return data[1]


print(l1.sort(key=function()))
