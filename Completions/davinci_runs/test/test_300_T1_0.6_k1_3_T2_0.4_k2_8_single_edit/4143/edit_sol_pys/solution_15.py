

import sys


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    ans = 0.0

    for n in range(N):
        tmp = A[n]
        for k in range(K):
            tmp *= 0.5
        ans += tmp

    print(int(ans))

if __name__ == "__main__":
    main()
