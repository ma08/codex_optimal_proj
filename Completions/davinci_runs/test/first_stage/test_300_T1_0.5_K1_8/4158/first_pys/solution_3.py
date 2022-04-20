

# SOLUTION
n = int(input())
a = list(map(int, input().split()))
a.sort()
d = {}
for i in range(n-1):
    for j in range(i+1, n):
        d[a[j] - a[i]] = d.get(a[j] - a[i], 0) + 1

ans = 0
for i in d:
    if d[i] > ans:
        ans = d[i]
        m = i

print(ans+1)
for i in a:
    if i % m == 0:
        print(i, end=' ')