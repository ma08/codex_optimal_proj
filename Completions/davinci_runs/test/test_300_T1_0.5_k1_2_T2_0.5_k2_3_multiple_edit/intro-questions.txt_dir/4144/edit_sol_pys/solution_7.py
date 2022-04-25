import sys
from collections import deque

sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7


# N, K = 8, 5
# A = [1, 2, 3, 4, 5, 6, 7, 8]


def solve(N, K, A):
    A.sort()
    queue = deque()
    queue.append((A[0], 1))
    res = 0
    for i in range(1, N):
        while queue:
            if queue[0][0] * A[i] > K:
                break
            queue.popleft()
        res += len(queue)
        res %= MOD
        queue.append((A[i], 1))
    return res


print(solve(N, K, A))
