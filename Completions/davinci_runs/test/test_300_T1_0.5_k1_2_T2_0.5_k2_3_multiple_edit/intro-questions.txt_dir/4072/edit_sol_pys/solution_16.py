def is_prime(n_):
    if n_ == 1:
        return 0
    if n_ == 2:
        return 1
    if n_ % 2 == 0:
        return 0
    for i in range(3, int(n_**0.5)+1, 2):
        if n_ % i == 0:
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
