

# ============
# Solution
# ============

a, b, k = input().split(' ')
a, b, k = int(a), int(b), int(k) + 1

# a_prime = gcd(a, b) + 1
a_prime = a if a < b else b - 1
b_prime = a if a > b else b - 1

while a_prime != 0:
    a_prime, b_prime = b_prime % a_prime, a_prime - 1

# The k-th largest number is a_prime / k
print(int(b_prime / k))
