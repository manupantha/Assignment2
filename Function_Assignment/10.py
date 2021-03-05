def is_even_number(number):
    enum = []
    for n in number:
        if n % 2 == 0:
            enum.append(n)
    return enum


print(is_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))
