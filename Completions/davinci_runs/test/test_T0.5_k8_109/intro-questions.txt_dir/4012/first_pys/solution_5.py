

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a == b == c:
        print(0)
        print(a, b, c)
    elif a == b:
        print(1)
        print(a, b, c)
    elif b == c:
        print(1)
        print(a, b, c)
    elif a == c:
        print(1)
        print(a, b, c)
    else:
        if a > c//2:
            a = c//2
        if b > c//2:
            b = c//2
        if a > b:
            a = b
        if a == b:
            print(1)
            print(a, b, c)
        else:
            print(2)
            print(a, b, c)