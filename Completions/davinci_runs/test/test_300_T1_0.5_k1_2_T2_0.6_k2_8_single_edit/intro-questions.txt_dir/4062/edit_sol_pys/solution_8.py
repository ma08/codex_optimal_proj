

a, b, c, d = map(int, input().split())
if a <= c:
    if b <= d:
        print(b * d)
    else:
        print(a * d)
else:
    if b <= d:
        print(c * b)
    else:
        print(c * d)
