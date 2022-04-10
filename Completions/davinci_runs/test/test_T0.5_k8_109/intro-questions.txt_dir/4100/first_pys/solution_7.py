

n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

# 各プレイヤーの正解数を数える
players = [0] * n
for a_i in a:
    players[a_i - 1] += 1

# 各プレイヤーのスコアを計算する
scores = [k - (q - p) for p in players]

# スコアが0以上なら生き残り、そうでなければ敗退
for score in scores:
    if score > 0:
        print('Yes')
    else:
        print('No')