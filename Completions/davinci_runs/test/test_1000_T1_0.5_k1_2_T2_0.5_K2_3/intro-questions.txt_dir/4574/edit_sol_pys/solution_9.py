
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] == a[j] or a[i] == a[j] + 1:
            continue
        ans = max(ans, a[i] * a[j])
print(ans)
