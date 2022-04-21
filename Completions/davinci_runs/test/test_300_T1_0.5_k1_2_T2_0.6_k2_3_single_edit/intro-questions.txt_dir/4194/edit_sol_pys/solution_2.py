
n, m = map(int, input().split())  # n: 平均値, m: 数値数
a = list(map(int, input().split()))
a.sort()
a.reverse()  # 降順に並べ替える
if a[0] > n:
    print(-1)  # m個の和がn以上になってしまったら-1
    exit()  # 終了
s = 0
for i in range(m):
    s += a[i]

print(n - s)
