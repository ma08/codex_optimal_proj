
import sys

S, W = map(int, sys.stdin.readline().split()) # S: 지능, W: 체력

if S <= W:
    print("unsafe")
else:
    print("safe")
