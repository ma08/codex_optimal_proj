

a, b, x = map(int, input().split())

if a + b > x:
    print(0)
    exit()

k = (x - b) // a
l = len(str(k))
print(k if a * k + b * l <= x else k - 10 ** (l - 1))
