

a, b, c, d = map(int, input().split())

e = max(a, b, c, d)
f = a + b + c + d - e
g = min(a, b, c, d)

print(e - f, f - g, g, sep=' ')
