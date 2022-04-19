
n, w = map(int, input().split())  # 入力
a = list(map(int, input().split()))  # 入力
i = 0  # インデックス
j = 0  # 合計値
for i in range(n):  # ループ
    if a[i] > w or a[i] < -w:  # ルールに反する場合
        print(0)  # 0を出力
        break  # ループを抜ける
    j += a[i]  # 合計値を更新
    if j > w or j < 0:  # 合計値がルールに反する場合
        print(0)  # 0を出力
        break  # ループを抜ける
if i == n-1:  # ループが最後まで回った場合
    print(w-j+1)  # 答えを出力
