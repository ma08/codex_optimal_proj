

def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    if n == 2:
        return True
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

n = int(input())
if is_prime(n):
    print(1)
else: print(0)
