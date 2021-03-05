def factorial(n1):
    if n1 == 0:
        return 1
    else:
        return n1 * factorial(n1 - 1)


n1 = int(input("Input a number to compute the factiorial : "))
print(factorial(n1))
