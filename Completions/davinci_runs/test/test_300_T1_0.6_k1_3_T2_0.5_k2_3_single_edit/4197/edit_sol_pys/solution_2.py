

import sys
import math
from collections import deque
from functools import reduce

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    n = NI()
    a = NLI()

#print(n)
#print(a)

ans = [-1] * n
count = 0

for i in range(n):
    ans[a[i]-1] = count
    count = count + 1

    print(' '.join(map(str,ans)))


if __name__ == "__main__":
    main()
