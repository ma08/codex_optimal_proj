
n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()

dist = []
for i in range(n):
    dist.append(abs(x - a[i]))
dist.sort()

ans = 0
for i in range(1, n):
    ans = max(ans, (dist[i] - dist[i - 1]) // 2)

print(ans)
