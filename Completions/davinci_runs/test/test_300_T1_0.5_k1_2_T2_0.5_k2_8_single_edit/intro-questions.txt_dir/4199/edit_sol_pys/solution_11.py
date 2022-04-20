import sys

N, K = list(map(int,sys.stdin.readline().split()))
h = list(map(int,sys.stdin.readline().split()))

count = 0
for i in range(N):
    if h[i] >= K:
        count += 1

print(count)
