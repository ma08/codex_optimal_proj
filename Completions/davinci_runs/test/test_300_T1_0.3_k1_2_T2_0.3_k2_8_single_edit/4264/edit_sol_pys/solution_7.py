

import math

N = int(input())

ans = 0

for i in range(1, N+1):
    if math.log10(i)+1 % 2 == 1: # 奇数の桁数の数を数える
        ans += 1

print(ans)
