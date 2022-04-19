

N, M, X = map(int, input().split())

A = list(map(int, input().split()))

k = (x - b) // a
l = len(str(k))

if a * k + b * l <= x:
    print(k)
else:
    print(k - 10 ** (l - 1))
