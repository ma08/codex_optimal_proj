
import numpy as np

n = int(input())
d_list = list(map(int, input().split())) # array([1, 2, 3])

s = 0
for i in range(n):
    for j in range(i+1, n): # [1, 2, 3]
        s += d_list[i] * d_list[j] # 1 * 2, 1 * 3, 2 * 3

print(s)
