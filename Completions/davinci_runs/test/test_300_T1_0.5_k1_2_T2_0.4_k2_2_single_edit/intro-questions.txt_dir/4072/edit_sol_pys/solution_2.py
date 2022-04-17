
def is_prime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return 0
    return 1

def is_prime_string(n):
    return is_prime(int(n)) or is_prime(int(n[::-1]))

a = input()
print(is_prime_string(a))
