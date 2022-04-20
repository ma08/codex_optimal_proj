

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

n = int(input())
b = list(map(int, input().split()))

a = []

for i in range(n):
    if is_prime(b[i]):
        a.append(b[i])
    else:
        a.append(b[i] // b[n - i - 1])

print(*a)
