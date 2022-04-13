
# 入力
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

# 各頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
# 各頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
# その頂点を含む辺の中で最も短い辺は、その頂点が含まれる連結成分の中で最も遠い頂点までの辺となる

# 各頂点を始点とした深さ優先探索を行い、各頂点について最も遠い頂点までの距離を求める
# その頂点を含む辺の中で最も短い辺の長さは、その頂点自身と最も遠い頂点までの距離となる

# 各頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
# その頂点を含む辺の中で最も短い辺は、その頂点が含まれる連結成分の中で最も遠い頂点までの辺となる

# 各頂点を始点とした深さ優先探索を行い、各頂点について最も遠い頂点までの距離を求める
# その頂点を含む辺の中で最も短い辺の長さは、その頂点自身と最も遠い頂点までの距離となる

# 各頂点を始点とした深さ優先探索を行い、各頂点について最も遠い頂点までの距離を求める
# その頂点を含む辺の中で最も短い辺の長さは、その頂点自身と最も遠い頂点までの距離となる

# 各頂点を始点とした深さ優先探索を行い、各頂点について最も遠い頂点までの距離を求める
# その頂点を含む辺の中で最も短い辺の長さは、その頂点自身と最も遠い頂点までの距離となる

# 各頂点を始点とした深さ優先探索を行い、各頂点について最も遠い頂点までの距離を求める
# その頂点を含む辺の中で最も短い辺の長さは、その頂点自身と最も遠い頂点までの距離となる

# 各頂点を始点とした深さ優先探索を行い、各頂点について最も遠い頂点までの距離を求める
# その頂点を含む辺の中で最も短い辺の長さは、その頂点自身と最も遠い頂点までの距離となる

# 各頂点を始点とした深さ優先探索を行い、各頂点について最も遠い頂点までの距離を求める
# その頂点を含む辺の中で最も短い辺の長さは、その頂点自身と最も遠い頂点までの距離となる



# 深さ優先探索
def dfs(v, p, d):
    # v: 現在の頂点
    # p: vの親
    # d: vから根までの距離

    # 根からvまでの距離を記録する
    dist[v] = d

    # vから辿れる頂点を全て調べる
    for e in edges[v]:
        # 親でない頂点について
        if e != p:
            # 再帰的に探索
            dfs(e, v, d + 1)


# 各頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
def solve():
    # 探索済みの頂点
    done = [False] * N

    # 各頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
    for i in range(N):
        # すでに探索済みの頂点はスキップ
        if done[i]:
            continue

        # 頂点iから辿れる頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
        dfs(i, -1, 0)

        # 探索済みにする
        done[i] = True

        # 頂点iから辿れる頂点のうち、最も遠い頂点vを探す
        v = 0
        # 頂点iから辿れる頂点のうち、最も遠い頂点vを探す
        for j in range(N):
            # 頂点jから辿れる頂点のうち、最も遠い頂点vを探す
            if dist[v] < dist[j]:
                # 頂点jから辿れる頂点のうち、最も遠い頂点vを探す
                v = j

        # 頂点vから辿れる頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
        dfs(v, -1, 0)

        # 探索済みにする
        done[v] = True

    res = 0
    # 辺の中で最も短い辺の長さを求める
    for i in range(M):
        # 辺の中で最も短い辺の長さを求める
        if dist[ab[i][0] - 1] > 1 and dist[ab[i][1] - 1] > 1:
            # 辺の中で最も短い辺の長さを求める
            res += 1

    return res

# 隣接リスト
edges = [[] for _ in range(N)]
# 各頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
for a, b in ab:
    # 各頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
    edges[a - 1].append(b - 1)
    # 各頂点について、その頂点を含む辺の中で最も短い辺の長さを求める
    edges[b - 1].append(a - 1)

# 各頂点を始点とした深さ優先探索を行い、各頂点について最も遠い頂点までの距離を求める
dist = [0] * N
# その頂点を含む辺の中で最も短い辺の長さは、その頂点自身と最も遠い頂点までの距離となる
print(solve())
