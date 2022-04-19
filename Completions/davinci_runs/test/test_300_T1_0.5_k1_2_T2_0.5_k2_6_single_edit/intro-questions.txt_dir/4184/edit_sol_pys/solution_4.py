

N = int(input())  # 数値
W = list(map(int, input().split()))  # リスト

min_diff = 100 * N  # 仮の最大値
for t in range(1, N):
    s1 = sum(W[:t])  # 左側の合計
    s2 = sum(W[t:])  # 右側の合計
    diff = abs(s1 - s2)  # 差の絶対値
    if diff < min_diff:  # 差が最小値より小さい時
        min_diff = diff  # 最小値を更新

print(min_diff)
