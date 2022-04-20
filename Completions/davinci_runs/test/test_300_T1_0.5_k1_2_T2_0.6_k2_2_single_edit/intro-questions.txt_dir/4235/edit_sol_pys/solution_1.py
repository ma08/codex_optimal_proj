

import sys
import os
import heapq
import math

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

f = sys.stdin
o = sys.stdout

def inp():
    return(int(f.readline()))

def inlt():
    return(list(map(int,f.readline().split())))

def insr():
    return(input())

def invr():
    return(map(int,f.readline().split()))

def dfs(V,G,vis,parent,child):
    vis[V] = 1
    for i in G[V]:
        if vis[i] == 0:
            parent[i] = V
            child[V].append(i)
            dfs(i,G,vis,parent,child)

def bfs(V,G,vis,parent,child):
    vis[V] = 1
    q = [V]
    while q:
        V = q.pop(0)
        for i in G[V]:
            if vis[i] == 0:
                parent[i] = V
                child[V].append(i)
                vis[i] = 1
                q.append(i)

def dfs_path(V,G,vis,path):
    vis[V] = 1
    for i in G[V]:
        if vis[i] == 0:
            path.append(i)
            dfs_path(i,G,vis,path)

def bfs_path(V,G,vis,path):
    vis[V] = 1
    q = [V]
    while q:
        V = q.pop(0)
        for i in G[V]:
            if vis[i] == 0:
                path.append(i)
                vis[i] = 1
                q.append(i)

def solve():
    n,m = invr()
    G = [[] for i in range(n+1)]
    parent = [0]*(n+1)
    child = [[] for i in range(n+1)]
    vis = [0]*(n+1)
    for i in range(m):
        u,v = invr()
        G[u].append(v)
        G[v].append(u)
    dfs(1,G,vis,parent,child)
    #bfs(1,G,vis,parent,child)
    #print(child)
    vis = [0]*(n+1)
    path = []
    dfs_path(1,G,vis,path)
    #bfs_path(1,G,vis,path)
    #print(path)
    for i in range(len(path)-1):
        if path[i+1] in child[path[i]]:
            print('YES')
            print('1'*(len(path)-1))
            return
    print('YES')
    print('0'*(len(path)-1),end='')
    for i in range(1,n+1):
        if i not in path:
            print('1',end='')

solve()
