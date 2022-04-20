
n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

players = [k] * n  # 各プレイヤーのポイントを格納するリスト

for i in range(q):  # 各クエリに対して
    for j in range(n):  # 各プレイヤーに対して
        if j + 1 != a[i]:  # 回答者でないプレイヤーに対して
            players[j] -= 1  # ポイントを1減らす

for i in range(n):  # 各プレイヤーに対して
    if players[i] <= 0:  # ポイントが0以下なら
        print("No")  # Noを出力
    else:  # そうでないなら
        print("Yes")  # Yesを出力
