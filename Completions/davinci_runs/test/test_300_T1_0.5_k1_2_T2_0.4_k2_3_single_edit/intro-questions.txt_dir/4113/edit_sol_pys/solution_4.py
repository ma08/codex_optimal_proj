

import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

import sys

n = int(sys.stdin.readline().rstrip())

if is_prime(n):
    print("Yes")
else:
    print("No")

# for i in range(n // 4 + 1):
#     if (n - 4 * i) % 7 == 0:
#         print("Yes")
#         sys.exit()

# print("No")
