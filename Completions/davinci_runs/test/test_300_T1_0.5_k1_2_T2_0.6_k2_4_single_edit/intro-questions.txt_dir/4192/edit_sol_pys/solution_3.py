import sys
import os


sys.stdin = open(os.path.join(sys.path[0], 'input.txt'), 'r')

d, t, s = map(int, sys.stdin.readline().split())

if d / s <= t:
    print("Yes")
else:
    print("No")
