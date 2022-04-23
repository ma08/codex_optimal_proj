
n,m,q = map(int, input().split())
s = [[0 for _ in range(m+1)] for _ in range(n)]

for _ in range(q):
    a,b,c,d = map(int, input().split())
    s[a-1][c-1] += d

for i in range(n):
    for j in range(1,m+1):
        s[i][j] += s[i][j-1]

for i in range(n):
    for j in range(1,m+1):
        s[i][j] += s[i-1][j]

ans = 0
for i in range(n):
    for j in range(i+1,n):
        ans = max(ans, s[j][m] - s[i][m] - s[j][i] + s[i][i])

print(ans)
