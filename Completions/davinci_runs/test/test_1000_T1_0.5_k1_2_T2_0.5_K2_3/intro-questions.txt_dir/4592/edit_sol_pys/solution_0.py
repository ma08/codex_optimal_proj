
import math

n = int(input())
factorial = math.factorial(n)
divisor_count = 0

for i in range(1, factorial+1):
    if factorial % i == 0:
        divisor_count += 1

print(divisor_count % (10**9+7))
