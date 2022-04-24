
import math

A, B, K = [int(input()) for _ in range(3)]

gcd = math.gcd(A, B)
divisors = [d for d in range(1, gcd + 1) if gcd % d == 0]
divisors.sort(reverse=True)

print(divisors[K - 1])
