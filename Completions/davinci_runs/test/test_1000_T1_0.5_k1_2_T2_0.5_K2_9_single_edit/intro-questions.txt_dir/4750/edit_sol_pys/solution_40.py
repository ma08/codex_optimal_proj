
n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    if a == b:
        print(a, c)
    elif c == d:
        print(a, c)
    elif a == c:
        print(a, b)
    elif b == d:
        print(a, b)
    elif a == d:
        print(a, c)
    elif b == c:
        print(a, b)
    else:
        print(a, c)
