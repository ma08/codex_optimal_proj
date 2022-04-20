



def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

import math

# Get inputs
A, B, K = [int(input()) for _ in range(3)]

# Get GCD and all divisors
gcd_ = gcd(A, B)
divisors = [d for d in range(1, gcd_ + 1) if gcd_ % d == 0]
divisors.sort(reverse=True)

# Print K-th largest positive integer that divides both A and B.
print(divisors[K - 1])
