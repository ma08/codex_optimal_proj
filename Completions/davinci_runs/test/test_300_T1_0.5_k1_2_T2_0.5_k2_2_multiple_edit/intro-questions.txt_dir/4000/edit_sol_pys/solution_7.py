

import random
import sys

def get_max_edges(v1, v2):
    cnt1, edges1 = dfs(v1, -1)
    cnt2, edges2 = dfs(v2, -1)
    return edges1 + edges2 + cnt1 * cnt2



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



def generate_tree():
    n = random.randint(1, 10 ** 5)
    tree = [[] for _ in range(n)]
    for i in range(n - 1):
        v1, v2 = random.randint(1, n), random.randint(1, n)
        tree[v1 - 1].append(v2 - 1)
        tree[v2 - 1].append(v1 - 1)
    return tree


ans = 0
ans1, ans2, ans3 = -1, -1, -1

for it in range(10 ** 3):
    tree = generate_tree()
    n = len(tree)
    for v1 in range(n):
        for v2 in tree[v1]:
            for v3 in tree[v2]:
                if v1 != v3:
                    cur = get_max_edges(v1, v2) + get_max_edges(v1, v3) + get_max_edges(v2, v3)
                    if cur > ans:
                        ans = cur
                        ans1, ans2, ans3 = v1, v2, v3

# n = int(input())
# tree = [[] for _ in range(n)]
#
# for i in range(n - 1):
#     v1, v2 = map(int, input().split())
#     tree[v1 - 1].append(v2 - 1)
#     tree[v2 - 1].append(v1 - 1)
#
# ans = 0
# ans1, ans2, ans3 = 0, 0, 0
# for v1 in range(n):
#     for v2 in tree[v1]:
#         for v3 in tree[v2]:
#             if v1 != v3:
#                 cur = get_max_edges(v1, v2) + get_max_edges(v1, v3) + get_max_edges(v2, v3)
#                 if cur > ans:
#                     ans = cur
#                     ans1, ans2, ans3 = v1, v2, v3

print(ans)
print(ans1 + 1, ans2 + 1, ans3 + 1)
