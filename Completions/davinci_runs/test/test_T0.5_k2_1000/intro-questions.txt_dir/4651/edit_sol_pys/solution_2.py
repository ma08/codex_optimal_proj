

from sys import stdin
from itertools import permutations

q = int(stdin.readline())

for _ in range(q):
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))
    p = list(permutations(p))  # generate all possible permutations
    p.sort()  # sort the permutations
    print(*p[0])  # print the first element of the sorted permutations
