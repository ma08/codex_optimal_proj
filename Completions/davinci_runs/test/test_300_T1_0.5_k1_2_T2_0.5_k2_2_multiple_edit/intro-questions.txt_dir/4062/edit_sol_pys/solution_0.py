

a, b, c, d = map(int, input().split())
if a <= c <= b and a <= d <= b:
    print(b * d)
elif c <= a <= d and c <= b <= d:
    print(d * b)
elif c <= a <= d and a <= b <= d:
    print(d * a)
elif a <= c <= b and c <= d <= b:
    print(b * c)
