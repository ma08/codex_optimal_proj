

import sys

sys.setrecursionlimit(10**5)


def dfs(v, p):
    for i in range(len(graph[v])):
        u = graph[v][i]
        if u == p:
            continue
        dfs(u, v)
        if cnt[u] > 0:
            cnt[v] += cnt[u]
            cnt[u] = 0


def dfs2(v, p, up):
    cnt[v] = up
    for i in range(len(graph[v])):
        u = graph[v][i]
        if u == p:
            continue
        dfs2(u, v, up + 1 if cnt[u] == 0 else 0)



n = int(input())
x = [int(i) for i in input().split()]

#print(n, x)

min_cnt = 0
max_cnt = 0

# min
curr = x[0]
min_cnt = 1
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        min_cnt += 1

# max
curr = x[0]
max_cnt = 1
for i in range(1, len(x)):
    if x[i] != curr:
        curr = x[i]
        max_cnt += 1
    elif x[i] == curr and i == len(x)-1:
        max_cnt += 1

print(min_cnt, max_cnt)
