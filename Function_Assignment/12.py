n1 = int(input("enter the number : "))
n2 = int(input("enter the unknown number"))


def function(n2):
    return lambda n1: n1 * n2


s = function(n2)
print(s(n1))
