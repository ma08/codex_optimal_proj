
import math

a, b, k = [int(input()) for _ in range(3)]

# Get GCD and all divisors
gcd = math.gcd(a, b)
divisors = [d for d in range(1, gcd + 1) if gcd % d == 0]
divisors.sort(reverse=True)

# Print k-th largest positive integer that divides both a and b.
print(divisors[k - 1])
