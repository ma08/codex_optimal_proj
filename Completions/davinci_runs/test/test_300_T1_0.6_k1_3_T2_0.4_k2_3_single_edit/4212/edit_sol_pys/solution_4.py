import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = 10**10

n,m,q = map(int, input().split())
s = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(q):
    a,b,c,d = map(int, input().split())
    s[a-1][c-1] += d

for i in range(n):
    for j in range(1,m):
        s[i][j] += s[i][j-1]

for i in range(1,n):
    for j in range(m):
        s[i][j] += s[i-1][j]

ans = 0
for i in range(n):
    for j in range(i+1,n):
        ans = max(ans, s[j][m-1] - s[i][m-1] - s[j][i] + s[i][i])

print(ans)
