
import sys

k, x = map(int, sys.stdin.readline().split())

if k * 500 >= x:
    print("Yes")
else:
    print("No")
