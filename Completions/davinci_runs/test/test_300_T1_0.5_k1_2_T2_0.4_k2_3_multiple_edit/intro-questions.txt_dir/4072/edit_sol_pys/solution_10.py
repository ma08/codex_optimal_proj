

def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def is_prime_string(n):
    if is_prime(int(n)):
        return 1
    if is_prime(int(n[::-1])):
        return 1
    return 0

a = input()
print(is_prime_string(a))
