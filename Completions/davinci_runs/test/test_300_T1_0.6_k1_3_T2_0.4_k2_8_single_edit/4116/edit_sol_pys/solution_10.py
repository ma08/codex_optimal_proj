
from sys import stdin
from math import sqrt

def isInt(x):
    return int(x) == x

N = int(stdin.readline())

if isInt(sqrt(N)):
    print("Yes")
else:
    print("No")
