

a, b, c, d = map(int, input().split())

if (a <= c <= b <= d) or (c <= a <= d <= b):
    print(b * d, end=' ')
    print(a * c)
elif (a <= c <= d <= b) or (c <= a <= b <= d):
    print(d * b, end=' ')
    print(a * d, end=' ')
    print(c * b)
else:
    print(a * c)
