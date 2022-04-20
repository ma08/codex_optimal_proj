

import math

N = int(input())

ans = 0

for i in range(1, N+1):
    if math.log10(i)+1 % 2 == 1:  # 奇数桁の数字の数
        ans += 1

print(ans)
