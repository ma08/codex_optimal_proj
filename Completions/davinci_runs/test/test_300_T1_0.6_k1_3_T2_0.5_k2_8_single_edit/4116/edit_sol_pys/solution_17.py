
from sys import stdin
from math import sqrt, floor

N = int(stdin.readline())

if floor(sqrt(N)) == sqrt(N):
    print("Yes")
else:
    print("No")
