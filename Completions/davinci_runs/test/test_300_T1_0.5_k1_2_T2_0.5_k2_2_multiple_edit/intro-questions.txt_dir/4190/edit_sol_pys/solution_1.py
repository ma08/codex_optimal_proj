from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    d = defaultdict(int)
    for i in range(n):
        d[A[i]] += 1

    for i in range(n):
        if d[i] == 0:
            print(i)


if __name__ == '__main__':
    resolve()
