
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = list(map(int, input().split()))

x = [0] * m
for i in range(n):
    for j in range(m):
        x[j] = max(x[j], a[i][j])

ans = 10 ** 10
for i in range(n):
    sm = 0
    for j in range(m):
        if a[i][j] < x[j]:
            sm = 10 ** 10
            break
        sm += c[i]
    ans = min(ans, sm)

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)
