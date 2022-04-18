import math

N = int(input())  # number of terms

e = 1
for n in range(1, N+1):
    e += 1 / math.factorial(n)

print(e)
