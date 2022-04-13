n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n - 3):
    for j in range(i + 1, n - 2):
        if a[i] == a[j]:
            continue
        k = j + 1
        while k < n - 1 and a[i] != a[k]:
            k += 1
        if k == n - 1:
            continue
        for l in range(k + 1, n):
            if a[i] != a[l] and a[j] != a[l]:
                ans = max(ans, a[i] * a[j])

print(ans)
