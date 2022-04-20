

n, k = map(int, input().split())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = len(d) + 1
    a[i] = d[a[i]]

if len(d) < k:
    print("NO")
else:
    c = [0]*n
    for i in range(len(d)):
        for j in range(len(d[a[i]])):
            c[d[a[i]][j]] = i+1
    print("YES")
    print(" ".join(map(str, c)))
