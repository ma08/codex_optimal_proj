

N, X = list(map(int, input().split()))
x = list(map(int, input().split()))

x.sort()

dist = []
for i in range(N):

    dist.append(abs(X - x[i]))
dist.sort()

ans = 0
for i in range(1, N):
    ans = max(ans, (dist[i] - dist[i - 1]) // 2)

print(ans)
