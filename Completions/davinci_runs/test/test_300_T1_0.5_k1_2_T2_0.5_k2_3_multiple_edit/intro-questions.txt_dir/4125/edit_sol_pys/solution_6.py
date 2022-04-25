
N, X = list(map(int, input().split()))  # N: number of stores, X: position of the house
x = list(map(int, input().split()))     # x: position of stores

x.sort()

dist = []
for i in range(N):
    dist.append(abs(X - x[i]))
dist.sort()

ans = 0
for i in range(1, N):
    ans = max(ans, (dist[i] - dist[i - 1]) // 2)

print(ans)
