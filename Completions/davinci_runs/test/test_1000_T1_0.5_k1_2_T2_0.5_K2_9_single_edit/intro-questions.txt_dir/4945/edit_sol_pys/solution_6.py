
a, b = map(int, input().split())
m, sigma = map(int, input().split())

y = (sigma - 2) / 3
x = m - y
print(a*x + b*y)
