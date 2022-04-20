

import math

n = int(input())

# 平方根を求める。
sqrt_n = int(math.sqrt(n))

# 平方根以下の最大の数を求める。
for i in range(sqrt_n, 0, -1):
    if n % i == 0:
        break

# 数字の桁数を求める。
a = len(str(i))
b = len(str(n // i))

print(max(a, b))
