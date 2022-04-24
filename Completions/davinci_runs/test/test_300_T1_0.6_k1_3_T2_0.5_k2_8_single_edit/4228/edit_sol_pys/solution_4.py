
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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    A = NLI()
    A.sort()
    A.reverse()
    if N % 2 == 1:
        A = A[1:]
    B = []
    for i in range(N//2):
        B.append(A[2*i])
        B.append(A[2*i+1])
    B.reverse()
    ans = 0
    for i in range(N):
        ans += B[i] * B[(i+1)%N]
    print(ans)



def main():
    N = NI()
    A = NLI()

    ans = 0
    for i in range(N):
        ans += A[i] * (2 ** i)

    print(ans)


if __name__ == "__main__":
    main()
