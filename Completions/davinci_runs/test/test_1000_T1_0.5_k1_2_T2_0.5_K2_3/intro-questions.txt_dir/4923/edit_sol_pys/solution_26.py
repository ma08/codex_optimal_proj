

# # Read input
# n = int(input())
# a = list(map(int, input().split()))

# # Check if there are any unique numbers
# unique_numbers = set(a)
# if len(unique_numbers) == 1:
#     print("none")

# # If there are any unique numbers
# else:
#     # Find the highest unique number
#     for i in range(6, 0, -1):
#         if i in unique_numbers:
#             highest_unique = i
#             break

#     # Find the index of the highest unique number
#     for i in range(n):
#         if a[i] == highest_unique:
#             print(i + 1)
#             break

import math

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

print(prime_factors(100))
