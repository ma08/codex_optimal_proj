from collections import defaultdict


n, m = map(int, input().split())
a = list(map(int, input().split()))[::-1]
b = list(map(int, input().split()))[::-1]

d = [defaultdict(int) for _ in range(n)]
d[0][a[0]] = 1
d[0][b[0]] = 1

for i in range(1, n):
    for j in d[i - 1]:
        if j + a[i] <= m:
            d[i][j + a[i]] += d[i - 1][j]
        if j + b[i] <= m:
            d[i][j + b[i]] += d[i - 1][j]

print(sum(d[n - 1].values()))
