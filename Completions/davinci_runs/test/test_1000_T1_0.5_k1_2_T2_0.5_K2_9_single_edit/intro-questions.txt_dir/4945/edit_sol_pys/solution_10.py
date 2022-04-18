
a, b = map(int, input().split())
m, sigma = map(int, input().split())

if sigma <= 2:
    print(a*m)
else:
    if sigma % 3 == 0:
        y = (sigma - 2) / 3
        x = m - y
        print(a*x + b*y)
    else:
        y = (sigma - 2) / 3
        x = m - y
        print(a*x + b*y)
