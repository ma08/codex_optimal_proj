#coding:utf-8

from math import factorial

N = int(input())
fact = factorial(N)
divisor_count = 0

for i in range(1, fact+1):
    if fact % i == 0:
        divisor_count += 1

print(divisor_count % (10**9+7))
