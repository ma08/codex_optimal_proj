

from collections import deque
import sys

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
input = sys.stdin.readline

N, M = map(int, input().split())
stores = []
for _ in range(N):
    A, B = map(int, input().split())
    stores.append([A, B])

stores = sorted(stores, key=lambda x: x[0])

total = 0
for i in range(N):
    if M <= stores[i][1]:
        total += stores[i][0] * M
        break
    else:
        total += stores[i][0] * stores[i][1]
        M -= stores[i][1]

print(total)
