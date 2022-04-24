

import sys
import numpy as np

input = sys.stdin.readline

n, m = map(int, input().split())

a = np.zeros((n, m), dtype=np.int64)

for i in range(n):
    a[i] = np.array(list(map(int, input().split())))

ans = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            ans += 1

print(ans)
