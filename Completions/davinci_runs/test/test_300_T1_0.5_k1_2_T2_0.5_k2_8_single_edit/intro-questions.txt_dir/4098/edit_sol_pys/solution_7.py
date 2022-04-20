
from sys import stdin
from collections import deque
n, k = map(int, stdin.readline().split())
a = deque(map(int, stdin.readline().split()))


def solve(a, k):
    a.sort(reverse=True)
    if k == 1:
        return len(a)
    if k == 2:
        return max(len(a), a[0] + a[-1])
    if k == 3:
        return max(len(a), a[0] + a[-1] + a[-2])
    if k == 4:
        return max(len(a), a[0] + a[-1] + a[-2] + a[-3])
    return len(a)


print(solve(a, k)) 
