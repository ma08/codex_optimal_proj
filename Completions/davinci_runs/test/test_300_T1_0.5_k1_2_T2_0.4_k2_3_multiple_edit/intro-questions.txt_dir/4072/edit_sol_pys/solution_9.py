

def is_prime(n):
    return n % 2 == 0

def is_prime_string(n):
    return is_prime(int(n)) or is_prime(int(n[::-1]))

a = input()
print(is_prime_string(a))
