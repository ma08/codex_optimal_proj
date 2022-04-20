

# 入力
N, M = map(int, input().split())

# 各電球に接続されているスイッチのリスト
switches = []
for i in range(M):
    switches.append(list(map(int, input().split()))[1:])

# 各電球が点灯するかどうかのリスト
bulbs = list(map(int, input().split()))

# 各電球が点灯するかどうかを計算する
count = 0
for i in range(2 ** N):
    # 各電球が点灯しているかどうかのフラグ
    flag = True
    for j in range(M):
        # 各電球に接続されているスイッチの個数
        k = len(switches[j])
        # 各電球に接続されているスイッチがオンになっている個数
        on = 0
        for s in switches[j]:
            if (i >> (s - 1)) & 1:
                on += 1
        # 各電球が点灯しているかどうか
        if (on % 2) != bulbs[j]:
            flag = False
            break
    # 全ての電球が点灯している場合、カウントをインクリメント
    if flag:
        count += 1

# 出力
print(count)