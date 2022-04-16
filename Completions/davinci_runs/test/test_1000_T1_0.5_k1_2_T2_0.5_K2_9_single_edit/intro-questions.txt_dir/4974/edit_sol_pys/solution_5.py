

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

ans = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] <= m:
                ans.append(a[i] + a[j] + a[k])

print(max(ans))
