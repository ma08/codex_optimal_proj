

# from math import inf
from sys import stdin, stdout

# f = open("input.txt", "r")
# input = f.readline
# stdin = f

n, k = map(int, input().split())
# dna = [input().strip() for i in range(n)]
dna = list(map(str, stdin.read().splitlines()))
# print(dna)

# d = [[0 for i in range(n)] for j in range(n)]
d = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        d[i][j] = sum(1 for k in range(k) if dna[i][k] != dna[j][k])

# print(d)

# def mst(n):
#     used = [False for i in range(n)]
#     min_e = [inf for i in range(n)]
#     min_e[0] = 0
#     sel_e = []
#     for i in range(n):
#         v = -1
#         for j in range(n):
#             if not used[j] and (v == -1 or min_e[j] < min_e[v]):
#                 v = j
#         if min_e[v] == inf:
#             return sel_e
#         used[v] = True
#         sel_e.append((min_e[v], v))
#         for to in range(n):
#             min_e[to] = min(min_e[to], d[v][to])
#     return sel_e

# edges = mst(n)
# print(edges)
# print(sum(e for e, v in edges))

# def mst(n):
#     used = [False for i in range(n)]
#     min_e = [inf for i in range(n)]
#     min_e[0] = 0
#     sel_e = []
#     for i in range(n):
#         v = -1
#         for j in range(n):
#             if not used[j] and (v == -1 or min_e[j] < min_e[v]):
#                 v = j
#         if min_e[v] == inf:
#             return sel_e
#         used[v] = True
#         sel_e.append((min_e[v], v))
#         for to in range(n):
#             min_e[to] = min(min_e[to], d[v][to])
#     return sel_e

# edges = mst(n)
# print(edges)
# print(sum(e for e, v in edges))

def mst(n):
    used = [False for i in range(n)]
    min_e = [inf for i in range(n)]
    sel_e = []
    for i in range(n):
        v = -1
        for j in range(n):
            if not used[j] and (v == -1 or min_e[j] < min_e[v]):
                v = j
        if min_e[v] == inf:
            return sel_e
        used[v] = True
        sel_e.append((min_e[v], v))
        for to in range(n):
            min_e[to] = min(min_e[to], d[v][to])
    return sel_e


edges = mst(n)
# print(sum(e for e, v in edges))
for e, v in edges:
    print(e)
