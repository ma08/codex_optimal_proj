

n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    if a == b:
        print(a, c, b, d)
    elif c == d:
        print(a, c, b, d)
    elif a == c:
        print(a, b, c, d)
    elif b == d:
        print(a, b, c, d)
    elif a == d:
        print(a, c, b, d)
    elif b == c:
        print(a, b, c, d)
    else:
        print(a, c, b, d)
