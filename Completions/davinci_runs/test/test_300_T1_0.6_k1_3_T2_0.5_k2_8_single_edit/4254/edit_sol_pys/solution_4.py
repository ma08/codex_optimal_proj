
import sys

S = int(sys.stdin.readline())
W = int(sys.stdin.readline())

if S <= W:
    print("unsafe")
else:
    print("safe")
