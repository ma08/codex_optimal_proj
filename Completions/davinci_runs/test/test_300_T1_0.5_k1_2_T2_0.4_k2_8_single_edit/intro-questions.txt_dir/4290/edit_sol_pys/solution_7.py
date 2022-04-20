import sys

N, M = map(int, input().split())
if N == 0 or M == 0:
    sys.exit()


print(N * M)
