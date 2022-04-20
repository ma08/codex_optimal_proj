

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort()

ans = 0
for i in range(m):
    for j in range(1, n):
        ans = max(ans, abs(a[j][i] - a[j - 1][i]))
print(ans)