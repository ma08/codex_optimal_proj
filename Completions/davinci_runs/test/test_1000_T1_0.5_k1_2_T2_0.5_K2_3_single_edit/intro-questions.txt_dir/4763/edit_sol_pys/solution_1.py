

n = int(input())

if n % 3 != 0:
    print("impossible")
else:
    n //= 3
    if n > 20:
        print("triple", n // 3)
        n %= 3
    if n > 20:
        print("triple", n // 3)
        n %= 3
    if n > 20:
        print("triple", n // 3)
        n %= 3
    if n > 20:
        print("impossible")
    else:
        if n % 2 == 0:
            print("double", n // 2)
        else:
            print("single", n)
