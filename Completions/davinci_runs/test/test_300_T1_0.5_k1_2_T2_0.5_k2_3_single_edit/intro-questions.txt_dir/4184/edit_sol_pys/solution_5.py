

N = int(input())  # 入力した整数を変数Nに格納する
W = list(map(int, input().split()))  # 入力した整数を変数Wに格納する

min_diff = 100 * N  # min_diffを100 * Nに設定する
for t in range(1, N):  # 1からN-1までの範囲でループする
    s1 = sum(W[:t])  # 先頭からt番目までの要素を足し合わせてs1に格納する
    s2 = sum(W[t:])  # t番目から最後までの要素を足し合わせてs2に格納する
    diff = abs(s1 - s2)  # s1とs2の差をdiffに格納する
    if diff < min_diff:  # diffがmin_diffより小さい場合
        min_diff = diff  # min_diffにdiffを代入する

print(min_diff)  # min_diffを出力する
