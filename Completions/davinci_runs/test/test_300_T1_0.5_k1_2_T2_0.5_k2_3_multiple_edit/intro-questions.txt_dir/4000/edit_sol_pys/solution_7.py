import sys

sys.setrecursionlimit(2 * 10**5)

n = int(input())
tree = [[] for _ in range(n)]

for i in range(n - 1):
    v1, v2 = map(int, input().split()) - 1
    tree[v1].append(v2)
    tree[v2].append(v1)


def dfs(vertex, parent):
    # return (count of vertices in subtree, count of edges in subtree, max edges between subtree and parent)
    cnt = 1  # count of vertices in subtree
    edges = 0  # count of edges in subtree
    max_edges = 0  # max edges between subtree and parent
    for child in tree[vertex]:
        if child != parent:
            child_cnt, child_edges, child_max = dfs(child, vertex)
            cnt += child_cnt
            edges += child_edges + child_cnt  # count of edges in subtree
            max_edges = max(max_edges, child_max)  # max edges between subtree and parent
    return cnt, edges, max_edges + cnt


def get_max_edges(v1, v2):
    cnt1, edges1, max_edges1 = dfs(v1, -1)
    cnt2, edges2, max_edges2 = dfs(v2, -1)
    return edges1 + edges2 + max_edges1 + max_edges2


ans = 0
ans1, ans2, ans3 = 0, 0, 0
for v1 in range(n):
    for v2 in tree[v1]:
        for v3 in tree[v2]:
            if v1 == v3:
                continue
            cur = get_max_edges(v1, v2) + get_max_edges(v1, v3) + get_max_edges(v2, v3)
            if cur > ans:
                ans = cur
                ans1, ans2, ans3 = v1, v2, v3

print(ans)
print(ans1 + 1, ans2 + 1, ans3 + 1)
