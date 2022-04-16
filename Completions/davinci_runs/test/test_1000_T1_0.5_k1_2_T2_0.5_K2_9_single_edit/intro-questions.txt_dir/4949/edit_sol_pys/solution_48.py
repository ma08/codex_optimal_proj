
import sys

n, w, h = map(int, sys.stdin.readline().split())

for i in range(n):
    if int(sys.stdin.readline()) <= w or int(sys.stdin.readline()) <= h:
        print("DA")
    else:
        print("NE")
