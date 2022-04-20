

import math

N = int(input())

d = math.floor(math.log10(N)) + 1 # 10進数の桁数を求める
print(int(d))
