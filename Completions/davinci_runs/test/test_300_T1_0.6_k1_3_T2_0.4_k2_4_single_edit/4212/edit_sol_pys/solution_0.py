
n,m,q = map(int, input().split())
s = [[0 for _ in range(m+1)] for _ in range(n+1)]  # 各点への足し算値

for _ in range(q):
    a,b,c,d = map(int, input().split())
    s[a][c] += d  # 足し算値を更新

for i in range(1,n+1):  # 縦に足し算値を伝播
    for j in range(1,m+1):  # 横に足し算値を伝播
        s[i][j] += s[i][j-1]  # 左方向に伝播

for i in range(1,n+1):
    for j in range(1,m+1):
        s[i][j] += s[i-1][j]

ans = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        ans = max(ans, s[j][m] - s[i-1][m] - s[j][i-1] + s[i-1][i-1])

print(ans)
