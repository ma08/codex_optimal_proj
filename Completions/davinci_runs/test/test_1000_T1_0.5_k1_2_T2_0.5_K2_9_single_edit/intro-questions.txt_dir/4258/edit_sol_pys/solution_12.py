from collections import deque
from math import floor
from sys import stdin


def main():
    N, M, Q = map(int, stdin.readline().split())
    A = [list(map(int, stdin.readline().split())) for _ in range(Q)]
    ans = 0
    for i in range(M):
        for j in range(i + 1, M + 1):
            for k in range(M):
                for l in range(k + 1, M + 1):
                    if i >= k and j <= l:
                        continue
                    if k >= i and l <= j:
                        continue
                    tmp = 0
                    for m in range(Q):
                        if i <= A[m][1] <= j and k <= A[m][2] <= l:
                            tmp += A[m][0]
                    ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()
