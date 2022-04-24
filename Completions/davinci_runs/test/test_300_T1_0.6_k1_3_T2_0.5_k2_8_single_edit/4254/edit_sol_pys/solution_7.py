
import sys

S, W = map(int, input().split())

if S <= W:
    print("unsafe", end="")
else:
    print("safe", end="")
