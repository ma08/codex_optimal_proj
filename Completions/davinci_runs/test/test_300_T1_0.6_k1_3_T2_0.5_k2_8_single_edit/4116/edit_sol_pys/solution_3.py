

from sys import stdin
from math import sqrt


N = int(stdin.readline())

if sqrt(N).is_integer():
    print("Yes")
else:
    print("No")
