

import sys

def solve_problem(n, arr):
    inc_len = 1
    prev = arr[0]
    for i in range(1, n):
        if arr[i] > prev:
            inc_len += 1
        prev = arr[i]

    dec_len = 1
    prev = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] < prev:
            dec_len += 1
        prev = arr[i]

    return max(inc_len, dec_len)

n = int(input())
arr = list(map(int, input().split()))
print(solve_problem(n, arr))