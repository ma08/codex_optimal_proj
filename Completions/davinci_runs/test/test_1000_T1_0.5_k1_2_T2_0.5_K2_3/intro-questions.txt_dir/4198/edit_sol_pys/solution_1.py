a, b, x = map(int, input().split())

k = (x - b) // a

if k == 0:
    print(k)
    exit(0)

l = len(str(k))

if a * k + b * l <= x:
    if k <= 10 ** 9:
        print(k)
    else:
        print(10 ** 9)
else:
    if k - 10 ** (l - 1) <= 10 ** 9:
        print(k - 10 ** (l - 1))
    else:
        print(10 ** 9)
