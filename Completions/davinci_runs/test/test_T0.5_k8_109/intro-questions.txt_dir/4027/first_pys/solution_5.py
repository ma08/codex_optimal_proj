

n = int(input())

# The answer is the sum of the first n-1 numbers minus the last number.
# Proof:
# If n is even, then the answer is n/2 - n/2 = 0.
# If n is odd, then the answer is (n-1)/2 - (n+1)/2 = -1.
# The answer is always -1 or 0.
print((n-1) * (n // 2) - (n - (n // 2)) * (n // 2))