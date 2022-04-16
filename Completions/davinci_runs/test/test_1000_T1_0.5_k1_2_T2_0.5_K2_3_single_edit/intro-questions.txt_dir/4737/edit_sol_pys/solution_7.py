import sys
from itertools import permutations
import bisect


def solve(N, M, A, B):
    a_sum = [0] * (N + 1)
    b_sum = [0] * (N + 1)
    for i in range(N):
        a_sum[i + 1] = a_sum[i] + A[i]
        b_sum[i + 1] = b_sum[i] + B[i]
    ans = 0
    for i in range(N + 1):
        a_num = a_sum[i]
        b_num = M - a_num
        if b_num < 0:
            continue
        b_index = bisect.bisect_left(b_sum, b_num)
        if b_index != N + 1 and b_sum[b_index] == b_num:
            ans = max(ans, i + b_index)
        if b_index - 1 >= 0:
            ans = max(ans, i + b_index - 1)
    return ans

def main():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = solve(N, M, A, B)
    print(ans)

if __name__ == '__main__':
    main()
