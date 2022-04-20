import sys

import math

N = int(sys.stdin.readline())

ans = 0

for i in range(1, N+1):
    if math.log10(i)+1 % 2 == 1: # 偶数桁の数字は足さない
        ans += 1

print(ans)
