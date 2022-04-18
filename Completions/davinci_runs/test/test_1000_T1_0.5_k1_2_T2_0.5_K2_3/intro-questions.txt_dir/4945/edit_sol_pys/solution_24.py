
a, b = map(int, input().split())
m, sigma2 = map(int, input().split())

if sigma2 <= 2:
    print(a*m)
else:
    y = int((sigma2 - 2) / 3)
    x = m - y
    print(a*x + b*y)
