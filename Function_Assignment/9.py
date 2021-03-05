def test_prime(n1):
    if n1 == 1:
        return False
    elif n1 == 2:
        return True;
    else:
        for x in range(2, n1):
            if n1 % x == 0:
                return False
        return True


print(test_prime(int(input("number: "))))
