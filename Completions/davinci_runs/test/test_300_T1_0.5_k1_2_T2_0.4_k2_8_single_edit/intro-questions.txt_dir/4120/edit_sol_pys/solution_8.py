

# Solution 1

#!/usr/bin/python3

from copy import deepcopy

n, m, k = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

def dfs(v, g, used):
    used[v] = 1
    for i in range(len(g[v])):
        if (not used[g[v][i]]):
            dfs(g[v][i], g, used)

def is_connected(g):
    used = [0 for i in range(n)]
    dfs(0, g, used)
    for i in range(n):
        if (not used[i]):
            return False
    return True

def get_dist(g):
    dist = [0 for i in range(n)]
    used = [0 for i in range(n)]
    q = [0]
    used[0] = 1
    while (len(q) > 0):
        cur = q[0]
        q = q[1:]
        for i in range(len(g[cur])):
            if (not used[g[cur][i]]):
                used[g[cur][i]] = 1
                q.append(g[cur][i])
                dist[g[cur][i]] = dist[cur] + 1
    return sum(dist)

def get_answer(g, m, k):
    dist = get_dist(g)
    best = dist
    ans = []
    for i in range(1 << m):
        if (bin(i).count('1') == n - 1):
            cur = deepcopy(g)
            for j in range(m):
                if ((i >> j) % 2 == 1):
                    cur[g[j][0]].remove(g[j][1])
                    cur[g[j][1]].remove(g[j][0])
            if (is_connected(cur)):
                cur_dist = get_dist(cur)
                if (cur_dist < best):
                    best = cur_dist
                    ans = []
                    ans.append(i)
                elif (cur_dist == best):
                    ans.append(i)
    return ans

ans = get_answer(g, m, k)
print(len(ans))
for i in range(len(ans)):
    print(bin(ans[i])[2:].zfill(m))

# Reference: https://github.com/jaehyunp/stanfordacm/blob/master/code/RoadsNotOnlyInBerland.cpp

# Solution 2

#!/usr/bin/python3

import sys
import math

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for i in range(n)]
        self.dist = [0 for i in range(n)]
        self.best = 0
        self.ans = []

    def add_edge(self, a, b):
        self.edges[a].append(b)
        self.edges[b].append(a)

    def dfs(self, v, p):
        self.dist[v] = self.dist[p] + 1
        self.best += self.dist[v]
        for i in range(len(self.edges[v])):
            if (self.edges[v][i] != p):
                self.dfs(self.edges[v][i], v)

    def calc(self):
        self.dfs(0, -1)

    def remove_edge(self, a, b):
        self.edges[a].remove(b)
        self.edges[b].remove(a)

    def is_connected(self):
        used = [0 for i in range(self.n)]
        q = [0]
        used[0] = 1
        while (len(q) > 0):
            cur = q[0]
            q = q[1:]
            for i in range(len(self.edges[cur])):
                if (not used[self.edges[cur][i]]):
                    used[self.edges[cur][i]] = 1
                    q.append(self.edges[cur][i])
        for i in range(self.n):
            if (not used[i]):
                return False
        return True

    def get_answer(self, m, k):
        self.calc()
        for i in range(1 << m):
            if (bin(i).count('1') == self.n - 1):
                cur = Graph(self.n)
                cur.edges = [deepcopy(self.edges[i]) for i in range(self.n)]
                cur.dist = [deepcopy(self.dist[i]) for i in range(self.n)]
                for j in range(m):
                    if ((i >> j) % 2 == 1):
                        cur.remove_edge(self.edges[j][0], self.edges[j][1])
                if (cur.is_connected()):
                    cur.calc()
                    if (cur.best < self.best):
                        self.best = cur.best
                        self.ans = []
                        self.ans.append(i)
                    elif (cur.best == self.best):
                        self.ans.append(i)

n, m, k = list(map(int, input().split()))
g = Graph(n)
for i in range(m):
    a, b = list(map(int, input().split()))
    g.add_edge(a - 1, b - 1)
g.get_answer(m, k)
print(len(g.ans))
for i in range(len(g.ans)):
    print(bin(g.ans[i])[2:].zfill(m))

# Reference: https://github.com/jaehyunp/stanfordacm/blob/master/code/RoadsNotOnlyInBerland.cpp
