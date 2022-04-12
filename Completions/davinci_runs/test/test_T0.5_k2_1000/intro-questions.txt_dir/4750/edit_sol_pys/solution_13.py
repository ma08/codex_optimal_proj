n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    if a == b:
        print(a, c, end=' ')
    elif c == d:
        print(a, c, end=' ')
    elif a == c:
        print(a, b, end=' ')
    elif b == d:
        print(a, b, end=' ')
    elif a == d:
        print(a, c, end=' ')
    elif b == c:
        print(a, b, end=' ')
    else:
        print(a, c, end=' ')
