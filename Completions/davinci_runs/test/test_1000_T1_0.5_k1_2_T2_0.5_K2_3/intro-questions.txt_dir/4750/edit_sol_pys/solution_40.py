
n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    if a != b and a != c and a != d:
        print(a, c)
    elif b != a and b != c and b != d:
        print(a, c)
    elif c != a and c != b and c != d:
        print(a, b)
    elif d != a and d != b and d != c:
        print(a, b)
    else:
        print(a, c)
