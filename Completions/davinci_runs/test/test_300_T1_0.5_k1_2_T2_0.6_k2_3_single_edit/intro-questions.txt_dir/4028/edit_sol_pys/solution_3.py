

import sys
import collections

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
    B = NLI()
    C = NLI()
    A.sort()
    B.sort()
    C.sort()

    ans = 0
    for i in range(N):
        b = B[i]

        a_idx = bisect.bisect_left(A, b)
        c_idx = N - bisect.bisect_right(C, b)

        ans += a_idx * c_idx

    print(ans)

import math

def main():
    main()


if __name__ == "__main__":
    main()
