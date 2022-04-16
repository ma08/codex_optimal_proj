
import sys

n = int(input())
tree = [[] for _ in range(n)]

for i in range(n - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    tree[v1].append(v2)
    tree[v2].append(v1)


def dfs(vertex, parent):
    # return (count of vertices in subtree, count of edges in subtree)
    cnt = 1
    edges = 0
    for child in tree[vertex]:
        if child != parent:
            child_cnt, child_edges = dfs(child, vertex)
            cnt += child_cnt
            edges += child_edges + child_cnt
    return cnt, edges


def get_max_edges(v1, v2, v3):
    cnt1, edges1 = dfs(v1, v2)
    cnt2, edges2 = dfs(v2, v1)
    cnt3, edges3 = dfs(v3, v1)
    cnt4, edges4 = dfs(v3, v2)
    return edges1 + edges2 + edges3 + edges4 + cnt1 * cnt2 + cnt1 * cnt3 + cnt2 * cnt4



print(ans)
print(ans1 + 1, ans2 + 1, ans3 + 1)
