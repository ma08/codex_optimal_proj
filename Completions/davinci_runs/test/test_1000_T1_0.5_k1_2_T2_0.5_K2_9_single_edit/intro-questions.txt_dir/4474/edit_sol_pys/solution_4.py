
import sys
from math import log
from bisect import bisect_left

q = int(input())
for _ in range(q):
    n = int(input())
    print(3 ** (int(log(n, 3)) + 1))
