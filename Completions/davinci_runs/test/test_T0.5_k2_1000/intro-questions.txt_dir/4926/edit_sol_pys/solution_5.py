
import math

n = int(input())

e = 0
for i in range(n+1):
    e += 1 / math.factorial(i)

print(round(e, n))
