import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


N, M = map(int, input().split())

for i in range(N+1):
    if is_prime(i):
        print(i)
