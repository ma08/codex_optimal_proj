

t = int(input())

for _ in range(t):
    a, b, c = [int(x) for x in input().split()]
    # a < b < c

    # a is first
    if a < b < c:
        if b % a == 0 and c % b == 0:
            print(0)
            print(a, b, c)
        elif b % a == 0 and c % b != 0:
            print(1)
            print(a, b, b)
        elif b % a != 0 and c % b == 0:
            print(1)
            print(a, a, c)
        else:
            print(2)
            print(a, a, a)
    # b is first
    elif b < a < c:
        if a % b == 0 and c % a == 0:
            print(0)
            print(b, a, c)
        elif a % b == 0 and c % a != 0:
            print(1)
            print(b, a, a)
        elif a % b != 0 and c % a == 0:
            print(1)
            print(b, b, c)
        else:
            print(2)
            print(b, b, b)
    # c is first
    elif c < a < b:
        if a % c == 0 and b % a == 0:
            print(0)
            print(c, a, b)
        elif a % c == 0 and b % a != 0:
            print(1)
            print(c, a, a)
        elif a % c != 0 and b % a == 0:
            print(1)
            print(c, c, b)
        else:
            print(2)
            print(c, c, c)
    # a = b = c
    else:
        print(0)
        print(a, a, a)