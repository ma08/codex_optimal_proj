
import sys
from math import ceil


def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        A = list(map(int, sys.stdin.readline().strip().split()))
        print(solve(N, K, A))


def solve(N, K, A):
    A.sort()
    mid = ceil(len(A) / 2)
    if K <= mid:
        return A[mid-1]
    else:
        if A[mid] == A[mid-1]:
            return -1
        else:
            return A[mid]


main()
