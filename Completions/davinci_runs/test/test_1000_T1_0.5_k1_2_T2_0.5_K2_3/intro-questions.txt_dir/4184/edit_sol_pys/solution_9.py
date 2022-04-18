

N = int(input()) # 入力
W = list(map(int, input().split())) # 入力

min_diff = 100 * N # 最小値を初期化
for t in range(1, N):
    s1 = sum(W[:t])
    s2 = sum(W[t:])
    diff = abs(s1 - s2)
    if diff < min_diff:
        min_diff = diff
print(min_diff)
