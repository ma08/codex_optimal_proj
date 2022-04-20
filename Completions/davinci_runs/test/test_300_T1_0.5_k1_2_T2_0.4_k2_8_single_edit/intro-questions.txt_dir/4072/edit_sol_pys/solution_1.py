

def is_prime(n):
    if n == 1 or n == 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_prime_string(n):
    if is_prime(int(n)) or is_prime(int(n[::-1])):
        return True
    return False

a = input()
print(is_prime_string(a))
