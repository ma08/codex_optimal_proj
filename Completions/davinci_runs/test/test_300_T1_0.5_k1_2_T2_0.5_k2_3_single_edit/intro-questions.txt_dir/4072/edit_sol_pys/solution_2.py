
def is_prime(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return 0
        else:
            return 0

def is_prime_string(n):
    if is_prime(int(n)):
        return 1
    elif is_prime(int(n[::-1])):
        return 1
    return 0

a = input()
print(is_prime_string(a))
