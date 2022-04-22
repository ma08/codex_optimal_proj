

import sys
import math
from collections import deque
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    A = NLI()
    A = Counter(A)
    ans = 0
    for a in A.keys():
        if a < A[a]:
            ans += A[a] - a
        elif a > A[a]:
            ans += A[a]

    print(ans)


if __name__ == "__main__":
    main()
