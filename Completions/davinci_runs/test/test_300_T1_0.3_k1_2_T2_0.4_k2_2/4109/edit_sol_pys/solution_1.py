

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = list(map(int, input().split()))

x = [0] * m
for i in range(n):
    for j in range(m):
        x[j] = max(x[j], a[i][j])

ans = 10 ** 10
for i in range(n):
    sum = 0
    for j in range(m):
        if a[i][j] < x[j]:
            sum = 10 ** 10
            break
    sum += c[i]
    ans = min(ans, sum)

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)
