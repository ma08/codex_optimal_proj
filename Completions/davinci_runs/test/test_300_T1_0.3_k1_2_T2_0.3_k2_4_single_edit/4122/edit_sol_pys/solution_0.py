
# Solution

H, n = map(int, input().split())  # 初期HPとダメージの数
d = list(map(int, input().split()))  # ダメージ

for i in range(n):  # ダメージの数分繰り返す
    H += d[i]  # ダメージを受ける
    if H <= 0:  # HPが0以下になったら
        print(i + 1)  # 回数を出力して終了
        break
else:
    print(-1)  # 全てのダメージを受けてもHPが0以下にならなかったら-1を出力
