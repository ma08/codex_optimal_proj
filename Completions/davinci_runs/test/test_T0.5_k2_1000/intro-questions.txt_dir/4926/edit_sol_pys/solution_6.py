import math


n = int(input())

e = 1
for n in range(1, n+1):
    e += 1 / math.factorial(n)

print(e)
