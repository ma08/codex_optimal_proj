
n, k = map(int, input().split())
a = list(map(int, input().split()))

d = {}
for i in range(n):
    if a[i] in d:
        d[a[i]].append(i)
    else:
        d[a[i]] = [i]

if len(d) > k:
    print("NO")
else:
    c = [0]*n
    for i in range(1, len(d)+1):
        for j in range(len(d[i])):
            c[d[i][j]] = i
    print("YES")
    print(" ".join(map(str, c)))
