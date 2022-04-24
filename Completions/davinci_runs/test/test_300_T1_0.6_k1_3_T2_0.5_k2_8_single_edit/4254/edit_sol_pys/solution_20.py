
import sys

S, W = map(int, sys.stdin.readline().split())

if S <= W:  # 아주 간단한 조건문
    print("unsafe")
else:
    print("safe")
