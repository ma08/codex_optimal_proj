
N = int(input())  # 1行目のNを取得
ans = 0  # 奇数の個数をカウント
for i in range(1, N+1):  # 1からNまでの値をループ
    if i % 2 != 0:  # 奇数の場合
        ans += 1  # 奇数の個数をカウント
print(ans / N)  # 奇数の個数をNで割って出力
