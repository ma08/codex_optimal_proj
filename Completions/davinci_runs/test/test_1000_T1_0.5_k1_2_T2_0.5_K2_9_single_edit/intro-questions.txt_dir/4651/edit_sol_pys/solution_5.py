
from math import sqrt
from itertools import combinations
from sys import stdin

q = int(stdin.readline())

for _ in range(q):
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    for c in combinations(a, k):
        print(sum(c))
    print()
