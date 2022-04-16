x1, x2, x3, x4 = map(int, input().split())

a = max(x1, x2, x3, x4) # a = max(x1, x2, x3, x4)
b = x1 + x2 + x3 + x4 - a
c = min(x1, x2, x3, x4) # c = min(x1, x2, x3, x4)

print(a - b, b - c, c)
