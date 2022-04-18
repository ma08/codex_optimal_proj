

import numpy as np

n = int(input())
a = list(map(int, input().split()))

a = np.array(a)
d = np.unique(a)

ans = 0
for i in d:
    ans += d[i] - 2

print(ans)
