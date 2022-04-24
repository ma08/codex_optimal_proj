import sys
sys.setrecursionlimit(10**6)

import itertools

def dfs(G, v, pre):
    if v in pre:
        return True
    pre.append(v)
    for next_v in G[v]:
        if dfs(G, next_v, pre):
            return True
    pre.pop()
    return False
import math

def calc_length(path):
    length = 0
    for i in range(len(path)-1):
        length += math.sqrt((path[i][0]-path[i+1][0])**2 + (path[i][1]-path[i+1][1])**2)
    return length

def main():
    n, m = map(int, input().split())
    G = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # print(G)

    for i in range(n):
        if dfs(G, i, []):
            print('Yes')
            exit()
    print('No')

if __name__ == "__main__":
    main()
