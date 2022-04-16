
import math
import heapq
from collections import deque
import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    for _ in range(k):
        c, d = map(int, sys.stdin.readline().split())

    for i in range(n):
        print(len(graph[i]), end=' ')

if __name__ == '__main__':
    main()
