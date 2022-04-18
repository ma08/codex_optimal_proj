import sys
import math

sys.setrecursionlimit(1000000)

N, K, Q = [int(i) for i in input().split()]


def check(n):
    if n == 0:
        return 0
    else:
        return n % 2 + check(n // 2)


def solve(n):
    if n == 0:
        return 0
    else:
        return solve(n - 1) + check(n)


players = [K] * N

for i in range(Q):
    A = int(input()) - 1
    players[A] += 1
    # for j in range(N):
    #     if j != A:
    #         players[j] -= 1


# for i in range(N):
#     if players[i] > 0:
#         print('Yes')
#     else:
#         print('No')

print(solve(5))
