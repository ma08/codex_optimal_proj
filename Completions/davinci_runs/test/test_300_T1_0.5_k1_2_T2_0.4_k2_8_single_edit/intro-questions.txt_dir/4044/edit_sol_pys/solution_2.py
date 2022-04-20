
# coding: utf-8
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 10min

MOD = 10 ** 9 + 7


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    ans = 0
    for i in range(N):
        ans += A[i] * (N - i)

    ans -= A[-1]

    return ans


if __name__ == '__main__':
    print(solve())

a, b, x = map(int, input().split())
