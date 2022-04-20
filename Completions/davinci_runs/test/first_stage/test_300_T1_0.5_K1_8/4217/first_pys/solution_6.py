

import sys

N, M = map(int, sys.stdin.readline().split())

foods = [0] * M

for i in range(N):
    K = int(sys.stdin.readline().split()[0])
    for j in range(K):
        foods[int(sys.stdin.readline().split()[j])-1] += 1

print(foods.count(N))