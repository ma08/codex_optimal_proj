

a, b, c, d = map(int, input().split())

if a >= c:
    x = a
else:
    x = c

if b <= d:
    y = b
else:
    y = d

print(x * y)