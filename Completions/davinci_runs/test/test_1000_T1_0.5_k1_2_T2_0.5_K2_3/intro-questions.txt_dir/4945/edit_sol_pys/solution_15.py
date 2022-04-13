
a, b = map(int, input().split())
m, sigma = map(float, input().split())

if sigma <= 3:
    print(a*m)
else:
    y = (sigma - 3) / 3
    x = m - y
    print(a*x + b*y)
