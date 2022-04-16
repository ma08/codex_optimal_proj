
import math



def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


def prime_factors(x):
    factors = []
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime(i) and x % i == 0:
            factors.append(i)
    return factors

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a_factors = prime_factors(a)
    b_factors = prime_factors(b)
    if a_factors == b_factors:
        print(1)
    else: 
        print(0)
