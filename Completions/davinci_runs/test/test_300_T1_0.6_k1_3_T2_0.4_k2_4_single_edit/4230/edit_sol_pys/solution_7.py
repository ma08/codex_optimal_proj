import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(0, 200):
    if x - i not in p:
        print(x - i)
        exit()
    elif x + i not in p:
        print(x + i)
        exit()
