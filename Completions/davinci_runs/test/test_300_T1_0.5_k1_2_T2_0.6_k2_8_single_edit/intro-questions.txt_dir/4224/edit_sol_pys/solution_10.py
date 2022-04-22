import numpy as np

x = int(input())
a = np.array([int(x) for x in input().split()])

print(a)
print(a[::-1])


N = int(input())
A = [int(x) for x in input().split()]

count = 0 # 回数

for i in A:
    while i % 2 == 0:
        i //= 2
        count += 1

print(count)
