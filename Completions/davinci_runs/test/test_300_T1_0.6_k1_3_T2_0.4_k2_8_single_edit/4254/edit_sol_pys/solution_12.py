import sys

S, W = map(int, sys.stdin.readline().split()) # 강수량, 일교차

if S <= W:
    print("unsafe")
else:
    print("safe")
