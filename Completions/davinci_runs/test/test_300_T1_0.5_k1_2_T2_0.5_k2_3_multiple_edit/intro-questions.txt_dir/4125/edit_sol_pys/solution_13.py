N = int(input())  # 入力
a = list(map(int, input().split()))  # 入力


ans = 0  # 初期化
for i in range(N):  # 偶数番目を足す
    if i % 2 == 0:  # 偶数番目
        ans += a[i]  # 足す
    else:  # 奇数番目
        ans -= a[i]  # 引く

for i in range(N):  # 偶数番目が正、奇数番目が負
    if i % 2 == 0:  # 偶数番目
        print(ans, end=" ")  # 正
    else:  # 奇数番目
        print(-ans, end=" ")  # 負
