n = int(input())

if n % 3 != 0:
    print("impossible")
else:
    n //= 3
    if n >= 3:
        print("triple", n // 3)
        n = n % 3
    if n >= 3:
        print("triple", n // 3)
        n = n % 3
    if n >= 3:
        print("triple", n // 3)
        n = n % 3
    if n >= 3:
        print("impossible")
    else:
        if n % 2 == 0:
            print("double", n // 2)
        else:
            print("single", n)
