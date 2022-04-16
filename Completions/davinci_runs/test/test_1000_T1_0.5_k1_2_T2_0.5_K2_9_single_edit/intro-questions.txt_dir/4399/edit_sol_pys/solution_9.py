

N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if a[i] == a[j] or a[j] == a[k] or a[i] == a[k]:
                continue
            if a[i] + a[j] + a[k] < ans:
                continue
            if a[i] + a[j] > a[k] and a[i] + a[k] > a[j] and a[j] + a[k] > a[i]:
                ans = a[i] + a[j] + a[k]

print(ans)
