

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_short(n):
    return n > 1 and all(n % i for i in range(2, n))

print(is_prime_short(int(input())))
