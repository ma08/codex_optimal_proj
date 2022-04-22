import sys
import math

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n = int(input())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_sum(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime(i) and is_prime(n - i):
            return True
    return False

def count_prime_sums(n):
    count = 0
    for i in range(6, n + 1, 2):
        if is_prime_sum(i):
            count += 1
    return count

print(count_prime_sums(n))
