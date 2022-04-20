

import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    A.sort()
    ans = 0
    for i in range(N-K+1):
        ans += A[i+K-1] - A[i]
    print(ans)


if __name__ == '__main__':
    main()
