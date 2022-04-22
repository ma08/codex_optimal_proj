

import sys
import re
import math
import string
import itertools
import collections
import bisect
import queue
import heapq
import time
import random
import copy

sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7

def inp(): return int(sys.stdin.readline())

def inp_list(): return list(map(int, sys.stdin.readline().split()))


def lcm(x, y): return (x * y) // math.gcd(x, y)


def comb(n, r): return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def perm(n, r): return math.factorial(n) // math.factorial(n - r)


def dist(x1, y1, x2, y2): return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def func(n, m, k):  # n:頂点数, m:辺の数, k:削除する辺の数
    def dfs(u):
        if visited[u]:
            return
        visited[u] = True
        for v in graph[u]:
            dfs(v)

    graph = [[] for i in range(n)]  # 隣接リスト
    for i in range(m):
        a, b = inp_list()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    visited = [False] * n  # 全ての頂点に訪れたかどうか
    dfs(0)  # 0番目の頂点から訪れることができる頂点を全て訪れる
    if False in visited:
        print(0)
        return

    diff = []  # 削除する辺を示すリスト
    for i in range(m):
        a, b = inp_list()
        tmp1 = graph[a - 1][:]  # 隣接リストのコピー
        tmp2 = graph[b - 1][:]  # 隣接リストのコピー
        graph[a - 1].remove(b - 1)  # 辺を削除
        graph[b - 1].remove(a - 1)

        visited = [False] * n  # 全ての頂点に訪れたかどうか
        dfs(0)  # 0番目の頂点から訪れることができる頂点を全て訪れる
        if False in visited:
            diff.append(i)  # 訪れることができない頂点がある場合はdiffに追加

        graph[a - 1] = tmp1  # 削除した辺を元に戻す
        graph[b - 1] = tmp2

    if len(diff) < k:  # 削除する辺の数がdiffより小さい場合
        print(len(diff))
        for i in diff:
            print('1' * (i + 1) + '0' * (m - i - 1))
    else:  # 削除する辺の数がdiffより大きい場合
        print(k)
        for i in range(k):
            print('1' * (diff[i] + 1) + '0' * (m - diff[i] - 1))


func(inp(), inp(), inp())
