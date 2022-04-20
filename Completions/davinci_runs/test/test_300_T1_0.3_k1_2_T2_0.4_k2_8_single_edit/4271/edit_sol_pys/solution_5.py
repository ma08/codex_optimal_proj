import math


n, m = map(int, input().split())
a = [0]
a.extend(list(map(int, input().split())))

b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = b[i - 1] + a[i]

for i in range(m):
    l, r = map(int, input().split())
    print(b[r] - b[l - 1])
