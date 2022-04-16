

n = int(input())

if n % 3 != 0:
    print("impossible")
else:
    n //= 3
        a = n // 3
        n = n % 3 * 3
        print("triple", a)
    if n > 20 and n % 3 == 0:
        a = n // 3
        n = n % 3 * 3
        print("triple", a)
    if n > 20 and n % 3 == 0:
        a = n // 3
        n = n % 3 * 3
        print("triple", a)
    if n > 20:
        print("impossible")
    else:
        if n % 2 == 0:
            print("double", n // 2)
        else:
            print("single", n)
