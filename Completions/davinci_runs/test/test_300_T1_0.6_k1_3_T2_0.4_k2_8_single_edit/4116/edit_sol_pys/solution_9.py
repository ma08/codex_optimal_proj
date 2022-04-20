
from sys import stdin
from math import sqrt, floor


def is_int(x):
    return floor(x) == x

N = int(stdin.readline())

if is_int(sqrt(N)):
    print("Yes")
else:
    print("No")
