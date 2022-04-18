

# ============
# Solution
# ============

a, b, k = input().split(' ')
a, b, k = int(a), int(b), int(k)

a_prime = a
b_prime = b

while a_prime != 0:
    a_prime, b_prime = b_prime % a_prime, a_prime

# The k-th largest number is b_prime / k
print(int(b_prime / k))
