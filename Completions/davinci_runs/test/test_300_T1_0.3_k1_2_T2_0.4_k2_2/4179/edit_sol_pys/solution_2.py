
n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    if sum([a[i][j] * b[j] for j in range(m)]) + c > 0:  # sum([a[i][j] * b[j] for j in range(m)]) の部分は、a[i][j] * b[j] と b[j] との積を全て足し合わせたもの
        ans += 1
print(ans)
