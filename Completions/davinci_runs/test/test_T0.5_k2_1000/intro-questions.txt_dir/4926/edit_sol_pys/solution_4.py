import math

n = int(input())

e = 1
for i in range(1, n+1):
    e += 1 / math.factorial(i)

print(e)
