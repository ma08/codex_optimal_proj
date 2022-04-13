n, k = map(int, input().split())  # int型に変換してn,kに代入
a = list(map(int, input().split()))  # int型に変換してリストaに代入

ans = 0
for i in range(n):
    if a[i] % 2 == 1:  # 奇数の時
        a[i] -= 1  # 奇数を偶数にする
        ans += 1  # 奇数を偶数にするために費やした操作回数

if sum(a) // k < 2:
    print(ans)
else:
    print(ans + sum(a) // k - 1)
