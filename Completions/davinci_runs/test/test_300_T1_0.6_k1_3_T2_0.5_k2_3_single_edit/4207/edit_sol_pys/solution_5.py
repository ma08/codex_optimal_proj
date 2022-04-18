

import sys

sys.setrecursionlimit(10 ** 7)

def solve(n, a, b):
    pos = [[] for _ in range(n)]
    neg = [[] for _ in range(n)]
    zero = [[] for _ in range(n)]
    for i in range(n):
        if b[i] > 0:
            pos[i].append(b[i] / a[i])
        elif b[i] < 0:
            neg[i].append(b[i] / a[i])
        else:
            zero[i].append(i)

    for i in range(n):
        pos[i].sort()
        neg[i].sort()

    dp = [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(n)]
    res = dfs(0, 0, 0, n, pos, neg, zero, dp)
    return res

    if len(zero) > 0:
        res += len(zero) - 1

    return res


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))


if __name__ == "__main__":
    main()
