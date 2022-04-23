
N, M = map(int, input().split())
a = [int(input()) for _ in range(N)]

a.sort()
ans = 0

for i in range(M):
    if a[i] < 0:
        ans += a[i]

print(-ans)
