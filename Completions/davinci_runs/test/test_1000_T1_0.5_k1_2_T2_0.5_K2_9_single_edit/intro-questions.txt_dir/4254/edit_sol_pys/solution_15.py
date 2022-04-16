
import sys

sheep, wolves = map(int, sys.stdin.readline().split())

if sheep < wolves:
    print("unsafe")
else:
    print("safe")
