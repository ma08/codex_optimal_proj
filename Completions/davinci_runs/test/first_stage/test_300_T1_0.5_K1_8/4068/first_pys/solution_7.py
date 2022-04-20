

N, M = map(int, input().split())

# a_1, a_2, a_3, ..., a_M を読み込む
# 注意：a_1, a_2, a_3, ..., a_M は昇順にソートされている
broken_steps = sorted(int(input()) for _ in range(M))

# dp[n]: n階目までの移動方法の総数
# dp[0] = 1
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 5
# dp[5] = 8
# dp[6] = 13
dp = [0] * (N + 1)
dp[0] = 1

for i in range(0, N):
    if i + 1 <= N:
        dp[i + 1] += dp[i]
    if i + 2 <= N:
        dp[i + 2] += dp[i]

# broken_steps に含まれているステップをdpから引く
for step in broken_steps:
    dp[step] = 0

# dp[N]を出力
print(dp[N] % (10 ** 9 + 7))