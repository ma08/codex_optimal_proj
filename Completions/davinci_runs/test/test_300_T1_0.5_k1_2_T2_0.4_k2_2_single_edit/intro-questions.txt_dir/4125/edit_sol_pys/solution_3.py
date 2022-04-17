
N, X = list(map(int, input().split()))
Xs = list(map(int, input().split()))

dist = []
for i in range(N):
    dist.append(abs(X - Xs[i]))
dist.sort()

ans = 0
for i in range(1, N):
    ans = max(ans, (dist[i] - dist[i - 1]) // 2)

print(ans)
