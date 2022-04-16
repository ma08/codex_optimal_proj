

x1, x2, x3, x4, x5 = map(int, input().split())

a = max(x1, x2, x3, x4, x5)
b = x1 + x2 + x3 + x4 + x5 - a
c = min(x1, x2, x3, x4, x5)

print(a - b, b - c, c)
