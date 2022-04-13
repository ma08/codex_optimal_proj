

import sys

n = int(input())

if n == 1:
    print(0)
    sys.exit()

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(n, 10**6):
    if prime(i) and i % 10 != 1:
        print(i)
        sys.exit()

print(2)
