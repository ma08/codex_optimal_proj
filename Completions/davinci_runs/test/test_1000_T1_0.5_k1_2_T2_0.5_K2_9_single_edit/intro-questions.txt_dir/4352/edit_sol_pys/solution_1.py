


n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    total = c
    for j in range(m):
        total += b[j] * a[i][j]
    if total > 0:
        ans += 1
print(ans)
