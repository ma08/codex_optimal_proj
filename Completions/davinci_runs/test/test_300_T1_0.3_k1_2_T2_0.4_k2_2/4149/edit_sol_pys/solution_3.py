
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
a = list(map(int, input().split()))

b = []

for i in range(n):
    if is_prime(a[i]):
        b.append(a[i])
    else:
        b.append(a[i] // a[n + i])

print(*b)
