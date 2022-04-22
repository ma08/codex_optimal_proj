
a, b, x = map(int, input().split())

if a + b > x:
    print(0)
    exit()

n = (x - b) // a
l = len(str(n))

if a * n + b * l <= x:
    print(n)
else:
    print(n - 10 ** (l - 1))
