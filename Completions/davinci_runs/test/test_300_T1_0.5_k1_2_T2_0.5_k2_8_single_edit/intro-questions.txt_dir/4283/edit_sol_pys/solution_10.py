import math


# n = int(input())
# a = list(map(int, input().split()))
# a.sort()

# if n == 1:
#     print(1)
#     exit(0)

# i = 0
# j = 1

# count = 0
# while j < n:
#     if a[j] - a[i] <= 5:
#         j += 1
#     else:
#         i = j
#         j += 1
#     count = max(count, j - i)

# print(count)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)

    return primes


print(get_primes(100))
