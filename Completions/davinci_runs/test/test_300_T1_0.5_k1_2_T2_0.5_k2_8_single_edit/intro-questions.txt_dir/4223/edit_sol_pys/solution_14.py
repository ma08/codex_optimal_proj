

import sys
import numpy as np

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

b = np.array(a)
c = b.argsort()

ans = ""
for i in c:
    ans += str(a[i]) + " "

print(ans.strip())
