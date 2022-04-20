

# =============
# Solution 1
# =============

a, b, k = map(int, input().split())

# a_prime = gcd(a, b)
a_prime = a if a < b else b
b_prime = a if a > b else b

while a_prime != 0:
    a_prime, b_prime = b_prime % a_prime, a_prime

# The k-th largest number is a_prime / k
print(int(b_prime / k))
