import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    A = NLI()
    A.sort()
    B = NLI()
    B.sort()
    C = NLI()
    C.sort()

    # 各Bについて、Aから選べるものの最大数を二分探索で求める
    def bisearch_max(k):
        ng = -1
        ok = N
        while ok - ng > 1:
            mid = (ok+ng) // 2
            if A[mid] < k:
                ok = mid
            else:
                ng = mid
        return ok

    # 各Bについて、Cから選べるものの最大数を二分探索で求める
    def bisearch_min(k):
        ng = -1
        ok = M
        while ok - ng > 1:
            mid = (ok+ng) // 2
            if C[mid] <= k:
                ok = mid
            else:
                ng = mid
        return ok

    ans = 0
    for b in B:
        ans += bisearch_max(b) * (M - bisearch_min(b))
    print(ans)


if __name__ == "__main__":
    main()


n = int(input())
s = input()

count = 0

for i in range(n):
    if s[i:i+3] == 'ABC':
        count += 1

print(count)
