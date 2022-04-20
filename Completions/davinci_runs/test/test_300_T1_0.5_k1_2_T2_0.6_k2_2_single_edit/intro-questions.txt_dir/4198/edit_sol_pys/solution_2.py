

a, b = map(int, input().split())

if a + b > 753:
    print(0)
    exit()

k = (753 - b) // a
l = len(str(k))

if a * k + b * l <= 753:
    print(k)
else:
    print(k - 10 ** (l - 1))
