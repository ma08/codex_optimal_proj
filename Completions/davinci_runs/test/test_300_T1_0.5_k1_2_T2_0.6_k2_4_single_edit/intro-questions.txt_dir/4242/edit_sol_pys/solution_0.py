

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

ans = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        for k in range(n):
            ans[i][j] += a[i][k] * b[k][j]
