import math

N = int(input())

d = math.floor(math.log10(N)) + 1  # floor() 函数返回数字的下舍整数
print(int(d))
