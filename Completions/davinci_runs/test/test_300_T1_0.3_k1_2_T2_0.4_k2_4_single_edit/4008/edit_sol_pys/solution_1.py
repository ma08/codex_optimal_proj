

n, k = map(int, input().split())  # n - число вершин, k - число компонент связности
a = list(map(int, input().split()))  # список смежности

d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = []
    d[a[i]].append(i)
if len(d) < k:
    print("NO")
else:
    print("YES")
    c = [0] * n
    for i in range(1, k + 1):
        if i <= len(d):
            c[d[i][0]] = i
        else:
            c[d[1][i - len(d)]] = i
    print(*c)
