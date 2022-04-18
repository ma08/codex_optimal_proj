import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True



r, s = map(int, input().split())

if is_prime(r) and is_prime(s):
    print('Yes')
else:
    print('No')

