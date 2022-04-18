
from math import gcd
from functools import reduce

N = int(input())
A = tuple(map(int, input().split()))
print(sum(lcmm % a for a in A))
