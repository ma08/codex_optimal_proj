

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if a[i] != a[j] and a[j] != a[k] and a[i] != a[k]:
                ans = max(ans, a[i] * a[j] * a[k])
print(ans)
