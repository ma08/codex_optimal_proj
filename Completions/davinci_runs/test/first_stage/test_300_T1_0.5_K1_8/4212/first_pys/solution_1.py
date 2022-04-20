

from itertools import accumulate
from bisect import bisect_right

def main():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    for i in range(M):
        for j in range(i, M):
            score = 0
            for a, b, c, d in abcd:
                if i <= c < j:
                    score += d
            ans = max(ans, score)
    print(ans)

def main2():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    for i in range(M):
        for j in range(i, M):
            score = 0
            for a, b, c, d in abcd:
                if i <= c < j:
                    score += d
            ans = max(ans, score)
    print(ans)

def main3():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    for i in range(M):
        for j in range(i, M):
            score = 0
            for a, b, c, d in abcd:
                if i <= c < j:
                    score += d
            ans = max(ans, score)
    print(ans)

def main4():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    for i in range(M):
        for j in range(i, M):
            score = 0
            for a, b, c, d in abcd:
                if i <= c < j:
                    score += d
            ans = max(ans, score)
    print(ans)

if __name__ == '__main__':
    main()