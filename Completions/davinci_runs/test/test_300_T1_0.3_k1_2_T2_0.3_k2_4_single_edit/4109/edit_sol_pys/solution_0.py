

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = list(map(int, input().split()))

x = [0] * m
for i in range(n):
    for j in range(m):
        x[j] = max(x[j], a[i][j])

ans = 10 ** 10
for i in range(n):
    s = 0
    for j in range(m):
        if a[i][j] < x[j]:
            s = 10 ** 10
            break
        s += c[i]
    ans = min(ans, s)

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)
