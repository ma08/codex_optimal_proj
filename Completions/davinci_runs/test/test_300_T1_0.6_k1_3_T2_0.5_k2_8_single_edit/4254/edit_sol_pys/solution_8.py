
import sys

N = int(sys.stdin.readline())

for i in range(N):
    S, W = map(int, sys.stdin.readline().split())

    if S <= W:
        print("unsafe")
    else:
        print("safe")
