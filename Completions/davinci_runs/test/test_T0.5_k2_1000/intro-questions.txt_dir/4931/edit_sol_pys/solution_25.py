import sys

x, y = map(int, sys.stdin.readline().split())

if y == 1:
    print("IMPOSSIBLE") if x != 0 else print("ALL GOOD")
else:
    print(x / (y - 1))
