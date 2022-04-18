
#
import sys

n, w, h = map(int, input().split())

for i in range(n):
    if int(input()) <= w or int(input()) <= h or int(input()) <= w:
        print("DA")
    else:
        print("NE")
