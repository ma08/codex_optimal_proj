import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

for i in range(n):
    if f[i] == 0:
        for j in range(1, n+1):
            if j not in f:
                f[i] = j
                break

print(*f)
