n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * m
for i in range(n):  # 行
    for j in range(m):  # 列
        ans[j] += a[i][j]

for i in range(m):
    print(ans[i])
