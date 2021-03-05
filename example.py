from functools import reduce


# def add(*args, **kwargs):
#     print(kwargs)
#     print(args)
#     print(sum(kwargs.values()))
#
#
# add(1, 2, a=3, b=4)
#
# def add(*args):
#     print(args)
#
# add(1,2)
# add(1,2,3)
# add(1,2,3,4)
#
# def add_two(x):
#     return x + 2
#
#
# print(list(map(add_two, [1, 2, 3])))
#
#
# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# r = filter(is_even, [1, 2, 3, 4, 5])
# print(list(r))
#
#
#
#
# def mul(x, y):
#     return x * y
#
#
# print(reduce(mul, [1, 2, 3, 4, 5]))
#
# print(list(map(lambda a:a+2,[1,2,3])))

# def decorate_me(func):
#     def inner_func():
#         print("it is the decorator")
#         func()
#
#     return inner_func
#
#
# @decorate_me
# def ordinary():
#     print("ordinary")
#
#
# # ordinary = decorate_me(ordinary)
# ordinary()

def to_uppercase(func):
    def inner_func(s):
        a = func(s).upper()
        print(a)
    return inner_func

def echo(message):
    return message


echo = to_uppercase(echo)
echo(input("string"))
