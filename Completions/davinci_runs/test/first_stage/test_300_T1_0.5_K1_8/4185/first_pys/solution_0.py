

# Solution

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        ans += abs(a[i][j] - (i * m + j + 1))
print(ans // 2)