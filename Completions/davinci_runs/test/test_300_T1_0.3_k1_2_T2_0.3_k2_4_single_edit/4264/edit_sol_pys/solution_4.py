
import math

N = int(input())

ans = 0

for i in range(1, N+1):
    if math.log10(i)+1 % 2 == 1:  # 小数点以下の桁数を調べる
        ans += 1

print(ans)
