

a, b, x = map(int, input().split())

if a + b <= x:
    k = (x - b) // a
    l = len(str(k))

k = (x - b) // a
l = len(str(k))

if a * k + b * l <= x:
    print(k)
else:
    print(k - 10 ** (l - 1))
