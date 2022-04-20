
from sys import stdin

from math import sqrt, floor

def isInt(x):
    return floor(x) == x

N = int(stdin.readline())

if isInt(sqrt(N)):
    print("Yes")
else:
    print("No")
