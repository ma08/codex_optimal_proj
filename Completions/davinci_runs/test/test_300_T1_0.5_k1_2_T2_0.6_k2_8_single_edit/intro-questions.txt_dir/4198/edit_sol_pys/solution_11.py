

a, b, x = map(int, input().split())

if a + b > x:
    print(0)
    exit()

k = (x - b) // a
l = len(str(k))

if a * k + b * len(str(k)) <= x:
    print(k)
else:
    print(k - 10 ** (len(str(k)) - 1))
