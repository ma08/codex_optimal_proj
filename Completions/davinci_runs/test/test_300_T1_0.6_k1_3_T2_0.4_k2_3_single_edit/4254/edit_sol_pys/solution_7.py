
import sys

S, W = map(int, sys.stdin.readline().rstrip().split())

if S <= W:
    print("unsafe")
else:
    print("safe")
