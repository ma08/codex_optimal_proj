
a, b, c, d = map(int, input().split())

if b + c > a - d:
    print(b + c - a + d)
else:
    print(0)
