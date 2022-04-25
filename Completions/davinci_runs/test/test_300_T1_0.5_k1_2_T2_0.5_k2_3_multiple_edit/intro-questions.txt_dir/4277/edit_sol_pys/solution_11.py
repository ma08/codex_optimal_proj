

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

A.sort()

def min_expenses(N, M, A):
    d = deque(A)
    ans = 0
    for _ in range(M):
        min_cost = d.popleft()
        ans += min_cost
        d.append(min_cost + 1)
    return ans


print(min_expenses(N, M, A))
