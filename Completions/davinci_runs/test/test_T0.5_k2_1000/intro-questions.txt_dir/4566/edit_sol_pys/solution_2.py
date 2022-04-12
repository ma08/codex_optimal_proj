
N, M = map(int, input().split())

# 各頂点の次数を格納する配列を用意
degree = [0] * (N)

for i in range(M):
    a, b = map(int, input().split())
    edge.append([a, b])
    # 次数を計算
    degree[a] += 1
    degree[b] += 1

# 次数を出力する
for i in range(1, N + 1):
    print(degree[i])
