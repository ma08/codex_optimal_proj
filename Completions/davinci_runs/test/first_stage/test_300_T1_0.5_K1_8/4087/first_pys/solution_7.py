

import sys

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

a = int(sys.stdin.readline())
n = a + 1
while sum_of_digits(n) % 4 != 0:
    n += 1
print(n)