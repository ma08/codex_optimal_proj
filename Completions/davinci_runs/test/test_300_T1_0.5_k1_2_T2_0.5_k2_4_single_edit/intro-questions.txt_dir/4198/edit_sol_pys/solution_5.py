

a, b, x = map(int, input().split())

if a * 1000000000 + b > x:
    print(0)
    exit()

k = (x - b) // a
l = len(str(k))

if a * k + b * l <= x:
    print(k)
else:
    print(k - 10 ** (l - 1))
