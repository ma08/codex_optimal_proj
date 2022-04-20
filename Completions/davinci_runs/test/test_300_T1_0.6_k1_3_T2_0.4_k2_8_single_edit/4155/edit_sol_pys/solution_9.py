import sys
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

# 隣接リスト
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = ab[i]
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# 訪問済みリスト
visited = [False] * N

# 同じ値のものをまとめる
for key in tmp_dict.keys():
    tmp_dict[key].sort()

# 同じ値のものをまとめたものを出力する
ans = []
for key in tmp_dict.keys():
    tmp_list = []
    for i in range(len(tmp_dict[key])):
        if i == 0:
            tmp_list.append(tmp_dict[key][i])
            tmp_list.append(tmp_dict[key][i])
        elif tmp_dict[key][i-1] + 1 == tmp_dict[key][i]:
            tmp_list[1] = tmp_dict[key][i]
        else:
            ans.append(tmp_list)
            tmp_list = []
            tmp_list.append(tmp_dict[key][i])
            tmp_list.append(tmp_dict[key][i])
    ans.append(tmp_list)

print(len(ans))
