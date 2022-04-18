

N, M = map(int, input().split())

# 入力された辺を格納する配列を定義する
edge = [[] for _ in range(M)]

# 各頂点の次数を格納する配列を定義する
degree = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    edge[i].append(a)
    edge[i].append(b)
    # 次数を計算する
    degree[a] += 1
    degree[b] += 1

# 次数を出力する
for i in range(1, N + 1):
    print(degree[i])
