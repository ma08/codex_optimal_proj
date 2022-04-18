#coding:utf-8
import math
N = int(input())

divisor_count = 0
for i in range(1, math.factorial(N)+1):
    if math.factorial(N) % i == 0:
        divisor_count += 1
print(divisor_count % (10**9+7))
