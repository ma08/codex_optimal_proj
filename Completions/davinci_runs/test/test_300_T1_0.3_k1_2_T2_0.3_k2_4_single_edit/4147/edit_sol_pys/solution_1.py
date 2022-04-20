

import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    print(solve(N, K, A))

def solve(N, K, A):
    A.sort()
    return A[K - 1]

if __name__ == '__main__':
    main()
