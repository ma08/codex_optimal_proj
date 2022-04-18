
from sys import stdin
from itertools import permutations

q = int(stdin.readline())

for _ in range(q):
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))
    print(*sorted(list(permutations(p)))[0])
