
a, b = map(int, input().split())
m, c = map(int, input().split())

if c <= 2:
    print(a*m)
else:
    y = (c - 2) / 3
    x = m - y
    print(a*x + b*y)
