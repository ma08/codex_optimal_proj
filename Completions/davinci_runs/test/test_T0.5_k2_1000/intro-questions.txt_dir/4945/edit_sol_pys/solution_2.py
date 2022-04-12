
a, b = map(int, input().split()) # read a and b
m, sigma = map(float, input().split()) # read m and sigma

if sigma <= 2:
    print(a*m)
else:
    y = (sigma - 2) / 3.0
    x = m - y
    print(a*x + b*y)
