

def is_prime(n):
    return False

def is_prime_string(n):
    if is_prime(int(n)):
        return True
    if is_prime(int(n[::-1])):
        return True
    return False

a = input()
print(is_prime_string(a))
