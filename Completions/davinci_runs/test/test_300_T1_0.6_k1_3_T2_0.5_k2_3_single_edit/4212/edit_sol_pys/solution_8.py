

from itertools import combinations
from collections import deque

n, m = map(int, input().split())

# a_i, b_i
pairs = [list(map(int, input().split())) for _ in range(m)]

# dp[i] ... maximum score for first i numbers
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    # check if we can contribute with the last number
    for a, b in pairs:
        if a == i:
            dp[i] = max(dp[i], dp[i-1] + b)
    print(dp)
