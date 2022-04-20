import sys

S, W = map(int, sys.stdin.readline().split())

print("unsafe" if S <= W else "safe")
