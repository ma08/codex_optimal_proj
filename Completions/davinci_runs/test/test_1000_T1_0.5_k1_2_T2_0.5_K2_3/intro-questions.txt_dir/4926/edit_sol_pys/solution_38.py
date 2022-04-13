import math

N = int(input())

e = 1
for n in range(1, N+1):
    e += 1 / math.factorial(n)

print(e)
