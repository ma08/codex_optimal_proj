

import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    X = list(map(int, sys.stdin.readline().split()))
    X.sort()
    ans = 0
    for i in range(M):
        if X[i] < 0:
            ans += abs(X[i])
            X[i] += abs(X[i])
        elif X[i] > 0:
            ans += abs(X[i] - 1)
            X[i] -= abs(X[i] - 1)
    print(ans)


if __name__ == '__main__':
    main()