

from sys import stdin
from collections import defaultdict


def read_ints():
    return list(map(int, stdin.readline().split()))


def read_int():
    return int(stdin.readline())


def read_str():
    return stdin.readline().strip()


def read_strs():
    return list(map(str, stdin.readline().split()))


def is_odd(n):
    return n % 2 == 1


def is_even(n):
    return n % 2 == 0


def median(n):
    if is_odd(n):
        return (n + 1) // 2
    else:
        return n // 2


n, m = read_ints()
arr = read_ints()

left_count = defaultdict(int)
right_count = defaultdict(int)

res = 0

for i, num in enumerate(arr):
    left_count[num] += 1
    right_count[arr[i]] += 1

    if left_count[m] > median(i+1):
        res += 1
    if right_count[m] > median(n - i):
        res += 1

print(res)