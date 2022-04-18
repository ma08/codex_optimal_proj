n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
b = [0 for _ in range(n)]
ans = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == 1:
            b[j] = 1
    c = 0
    for j in range(n):
        c += b[j]
    if c == n:
        ans += 1
print(ans)

