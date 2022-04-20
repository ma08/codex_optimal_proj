
import sys
import math


def solve(N, M, K):
    if N > M:
        N, M = M, N

    if K >= N:
        return 0

    for i in range(K + 1):
        a = N - i
        b = M - K + i
        if b > 0 and a % b == 0:
            return i

    return -1

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, K = [int(i) for i in sys.stdin.readline().split()]
        print(solve(N, M, K))

if __name__ == "__main__":
    main()
