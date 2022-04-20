

N, M = map(int, input().split())

# 各IDがどのゲートを通れるかを格納するリスト
# 通れるゲートがない場合は空のリストを格納
id_list = [[] for _ in range(N + 1)]

for _ in range(M):
    L, R = map(int, input().split())
    id_list[L].append(R)

# 各IDが通れるゲートの最大値を格納するリスト
max_list = [0] * (N + 1)

for i in range(1, N + 1):
    # IDが通れるゲートがない場合、最大値は0
    if len(id_list[i]) == 0:
        continue
    # IDが通れるゲートの最大値は、そのIDが通れるゲートの最大値の最大値
    max_list[i] = max(id_list[i])

# 各IDが通れるゲートの最小値を格納するリスト
min_list = [M + 1] * (N + 1)

for i in range(N, 0, -1):
    # IDが通れるゲートがない場合、最小値はM + 1
    if len(id_list[i]) == 0:
        continue
    # IDが通れるゲートの最小値は、そのIDが通れるゲートの最小値の最小値
    min_list[i] = min(id_list[i])

# 全てのゲートを通れるIDの数
count = 0

# 各IDについて調べる
for i in range(1, N + 1):
    # IDが通れるゲートがない場合、そのIDは全てのゲートを通れない
    if len(id_list[i]) == 0:
        continue
    # IDが通れるゲートの最小値が、IDよりも小さいゲートの最大値よりも大きい場合、そのIDは全てのゲートを通れる
    if min_list[i] > max_list[i - 1]:
        count += 1

print(count)