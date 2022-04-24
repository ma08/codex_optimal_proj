n = int(input())
d = list(map(int, input().split()))
d.sort()
ans = 0
for i in range(1, n - 1):
    ans += min(d[i] - d[i - 1], d[i + 1] - d[i])
ans += d[-1] - d[0]
print(ans)

