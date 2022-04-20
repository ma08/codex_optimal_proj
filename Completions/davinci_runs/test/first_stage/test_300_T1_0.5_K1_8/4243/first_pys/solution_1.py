

import math

X = int(input())

# 500円玉が何枚必要か
x500 = math.floor(X/500)
# 残りのお金
x = X - x500*500
# 5円玉が何枚必要か
x5 = math.floor(x/5)

print(x500*1000+x5*5)