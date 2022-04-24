
import sys

N, K = map(int,sys.stdin.readline().split())
h = map(int,sys.stdin.readline().split())

count = 0
for i in range(N):
    if h[i] >= K:
        count += 1

print(count)
