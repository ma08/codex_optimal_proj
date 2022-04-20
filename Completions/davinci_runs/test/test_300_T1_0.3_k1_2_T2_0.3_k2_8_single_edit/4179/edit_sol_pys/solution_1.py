
n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    if sum([a[i][j] * b[j] for j in range(m)]) + c > 0:  # 各行の各列の値を掛け合わせて合計を求める
        ans += 1
print(ans)
