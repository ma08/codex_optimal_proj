
import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_prime = 0
for i in range(m):
    if is_prime(b[i]):
        max_prime = max(max_prime, b[i])

print(max_prime)
