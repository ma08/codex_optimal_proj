

a, b, k = input().split(' ')
a, b, k = int(a), int(b), int(k)

# a_prime = gcd(a, b) = b if a < b else a
# b_prime = gcd(a, b) = a if a < b else b
a_prime = b if a < b else a
b_prime = a if a < b else b

while a_prime != 0:
    a_prime, b_prime = b_prime % a_prime, a_prime

# The k-th largest number is b_prime / k
print(int(b_prime / k))
