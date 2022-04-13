n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())

    if a == b and c == d:
        print(a, c)
    elif a == c and b == d:
        print(a, b)
    elif a == d and b == c:
        print(a, c)
    elif a == b:
        print(a, c)
    elif c == d:
        print(a, c)
    else:
        print(a, c)
