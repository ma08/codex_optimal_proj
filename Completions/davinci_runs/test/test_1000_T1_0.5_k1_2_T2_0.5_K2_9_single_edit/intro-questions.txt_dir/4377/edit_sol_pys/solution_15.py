

x1, x2, x3, x4 = map(int, input().split())

a = max(x1, x2, x3)
b = x1 + x2 + x3 - a
c = min(x1, x2, x3)

print(a - b, b - c, c)
