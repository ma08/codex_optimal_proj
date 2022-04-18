
a, b = map(int, input().split())
m, s = map(int, input().split())

if s <= 2:
    print(a*m)
else:
    y = (s - 2) // 3
    x = m - y
    print(a*x + b*y)
