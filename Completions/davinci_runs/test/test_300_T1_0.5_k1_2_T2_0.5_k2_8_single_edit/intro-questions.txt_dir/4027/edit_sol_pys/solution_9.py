import math


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

if n % 2 == 0:
    print(0)
else:
    print(1)
