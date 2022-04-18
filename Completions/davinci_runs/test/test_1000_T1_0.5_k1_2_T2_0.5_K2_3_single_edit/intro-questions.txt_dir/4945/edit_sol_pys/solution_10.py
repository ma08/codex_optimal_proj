
a, b = map(int, input().split())
m, sigma = map(int, input().split())

if sigma <= 2:
    print(a*m)
else:
    y = float(sigma - 2) / 3
    x = m - y
    print(a*x + b*y)
